/**
 * code-handbook — server.js
 */

const express      = require("express");
const http         = require("http");
const WebSocket    = require("ws");
const pty          = require("node-pty");
const path         = require("path");
const fs           = require("fs");
const cors         = require("cors");
const UAParser     = require("ua-parser-js");
const cookieParser = require("cookie-parser");
const { execSync } = require("child_process");

// ─── Config ───────────────────────────────────────────────────
const PORT         = process.env.PORT      || 8080;
const REPO_PATH    = process.env.REPO_PATH || '.';
const MAX_PROCS    = parseInt(process.env.MAX_PROCS || "10");
const IDLE_MS      = parseInt(process.env.IDLE_MS   || "300000");

const ADMIN_KEY    = process.env.ADMIN_KEY || "123456";

let activeProcesses = 0;

// ─── Runners por lenguaje ─────────────────────────────────────
const RUNNERS = {
  python: {
    ext:  ".py",
    run:  (f) => ({ cmd: "python3", args: ["-u", f] }),
    skip: ["template.py", "launcher.py", "utils.py"],
  },
  javascript: {
    ext:  ".js",
    run:  (f) => ({ cmd: "node", args: [f] }),
    skip: [],
  },
  typescript: {
    ext:  ".ts",
    run:  (f) => ({ cmd: "npx", args: ["ts-node", "--skip-project", f] }),
    skip: [],
  },
  cpp: {
    ext:  ".cpp",
    run:  (f) => ({
      cmd:  "bash",
      args: ["-c", `g++ -std=c++17 -o /tmp/cpp_out "${f}" && /tmp/cpp_out`],
    }),
    skip: ["utils.h", "xd.cpp"],
  },
  java: {
    ext:  ".java",
    run:  (f) => ({
      cmd:  "bash",
      args: ["-c", `javac "${f}" -d /tmp && java -cp /tmp ${path.basename(f, ".java")}`],
    }),
    skip: [],
  },
};

// ─── Sistema de Logs ──────────────────────────────────────────
const LOG_FILE = path.join(process.cwd(), 'accesos.log');

function registrarAcceso(req, contexto) {
  const parser = new UAParser(req.headers['user-agent']);
  const ua = parser.getResult();

  const ip = req.headers['x-forwarded-for']?.split(',')[0] || req.socket.remoteAddress || 'IP desconocida';
  const sistemaOperativo = ua.os.name ? `${ua.os.name} ${ua.os.version || ''}`.trim() : 'SO Desconocido';
  const hardware = ua.device.model ? `(${ua.device.vendor || ''} ${ua.device.model})` : '';
  const dispositivoFinal = `${sistemaOperativo} ${hardware}`.trim();
  const navegador = ua.browser.name ? `${ua.browser.name} ${ua.browser.version || ''}`.trim() : 'Navegador Desconocido';
  const fecha = new Date().toLocaleString('es-CL', { timeZone: 'America/Santiago' });

  // 1. Mostrar en consola
  console.log(`\n[+] ACCESO DETECTADO: ${contexto}`);
  console.log(` ├─ Fecha y Hora : ${fecha}`);
  console.log(` ├─ IP           : ${ip}`);
  console.log(` ├─ Dispositivo  : ${dispositivoFinal}`);
  console.log(` └─ Navegador    : ${navegador}`);

  // 2. Grabar en el archivo de forma permanente
  const lineaLog = `[${fecha}] | IP: ${ip} | Disp: ${dispositivoFinal} | Nav: ${navegador} | Acción: ${contexto}\n`;
  fs.appendFile(LOG_FILE, lineaLog, (err) => {
    if (err) console.error("Error al escribir el log:", err);
  });
}

// ─── Express ──────────────────────────────────────────────────
const app    = express();
const server = http.createServer(app);

const allowedOrigins = [
  "https://vlegend14.github.io",
  "http://localhost:4321",
  "http://localhost:3000",
  "https://code-handbook-production.up.railway.app/admin"
];

app.use(cors({
  origin: function (origin, callback) {
    if (!origin || allowedOrigins.includes(origin.toLowerCase())) {
      callback(null, true);
    } else {
      console.log("![CORS Bloqueado]:", origin);
      callback(new Error('No permitido por vLegend (CORS)'));
    }
  },
  methods: ['GET', 'POST'],
  credentials: true,
  allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

// Middleware global de monitoreo HTTP
app.use((req, res, next) => {
  if (req.url !== '/health') {
    registrarAcceso(req, `Peticion HTTP -> ${req.method} ${req.url}`);
  }
  next();
});

// ─── Endpoints ────────────────────────────────────────────────

// Endpoint de Salud (Protegido)
app.get("/health", (req, res) => {
  if (req.cookies.auth_token !== ADMIN_KEY && req.query.key !== ADMIN_KEY) {
    return res.status(403).json({ error: "[ ACCESO DENEGADO ] - Estructura sellada." });
  }
  res.json({ ok: true, active: activeProcesses });
});

// Endpoint de Debug (Protegido)
app.get("/debug-env", (req, res) => {
  if (req.cookies.auth_token !== ADMIN_KEY && req.query.key !== ADMIN_KEY) {
    return res.status(403).json({ error: "[ ACCESO DENEGADO ] - Estructura sellada." });
  }
  
  try {
    const python = execSync("python3 --version").toString();
    const gpp = execSync("g++ --version").toString();
    const java = execSync("java -version 2>&1").toString();
    const rootFiles = fs.readdirSync(path.resolve(REPO_PATH));
    
    res.json({
      status: "online",
      cwd: process.cwd(),
      repo_path_resolved: path.resolve(REPO_PATH),
      binaries: { python, gpp, java },
      files_at_repo: rootFiles
    });
  } catch (e) {
    res.status(500).json({ error: e.message, path: path.resolve(REPO_PATH) });
  }
});

// GET /api/languages
app.get("/api/languages", (_, res) => {
  try {
    const langs = [];
    const absoluteRepo = path.resolve(REPO_PATH);
    
    for (const [lang, cfg] of Object.entries(RUNNERS)) {
      const dir = path.join(absoluteRepo, lang);
      
      if (!fs.existsSync(dir)) continue;

      const files = fs.readdirSync(dir).filter(
        (f) => f.endsWith(cfg.ext) && !cfg.skip.includes(f)
      );
      if (files.length > 0) langs.push({ id: lang, count: files.length });
    }
    res.json(langs);
  } catch (error) {
    res.status(500).json({ error: "Error leyendo repo", details: error.message });
  }
});

// GET /api/modules/:lang
app.get("/api/modules/:lang", (req, res) => {
  const { lang } = req.params;
  const cfg = RUNNERS[lang];
  if (!cfg) return res.status(404).json({ error: "Lenguaje no soportado" });

  const dir = path.join(path.resolve(REPO_PATH), lang);
  if (!fs.existsSync(dir)) return res.json([]);

  const files = fs.readdirSync(dir)
    .filter((f) => f.endsWith(cfg.ext) && !cfg.skip.includes(f))
    .sort()
    .map((f) => ({
      name: f,
      title: f
        .replace(cfg.ext, "")
        .replace(/_/g, " ")
        .replace(/^(\d+)\s/, "$1 · "),
    }));

  res.json(files);
});

// ─── Panel de Admin y Login ────────────────────────── 

app.get("/admin", (req, res) => {
  if (req.cookies.auth_token !== ADMIN_KEY) {
    return res.send(`
      <!DOCTYPE html>
      <html lang="es">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Control de Acceso</title>
        <style>
          body { background: #050505; color: #2a4a7f; font-family: monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
          .login-box { background: #0a0a0a; border: 1px solid #1a1a1a; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: center; border-top: 3px solid #2a4a7f; border-radius: 4px; width: 300px; }
          h2 { margin-top: 0; font-size: 1.2rem; letter-spacing: 2px; }
          input { background: #111; border: 1px solid #333; color: #d1d1d1; padding: 12px; margin: 20px 0; width: 90%; text-align: center; font-family: monospace; outline: none; }
          input:focus { border-color: #2a4a7f; }
          button { background: #1a2a44; color: #fff; border: none; padding: 12px 20px; width: 100%; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; font-family: monospace; font-weight: bold; }
          button:hover { background: #2a4a7f; }
        </style>
      </head>
      <body>
        <form class="login-box" action="/admin/login" method="POST">
          <h2>[ RECONOCIMIENTO ]</h2>
          <input type="password" name="password" placeholder="Ingresa la llave" required autofocus>
          <button type="submit">Traspasar</button>
        </form>
      </body>
      </html>
    `);
  }

  let logsHtml = "<p style='color:#666;'>No hay registros.</p>";
  if (fs.existsSync(LOG_FILE)) {
    const contenido = fs.readFileSync(LOG_FILE, "utf8");
    const lineas = contenido.trim().split("\n").reverse(); 
    
    logsHtml = lineas.map(linea => {
      const match = linea.match(/^(\[[^\]]+\])(.*)/);
      if (match) {
        return `<div class="log-line"><span class="timestamp">${match[1]}</span>${match[2]}</div>`;
      }
      return `<div class="log-line">${linea}</div>`;
    }).join("");
  }

  res.send(`
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Admin</title>
      <style>
        body { background-color: #080808; color: #d1d1d1; font-family: monospace; margin: 0; padding: 20px; border-left: 8px solid #1a2a44; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #111; padding-bottom: 10px; margin-bottom: 20px; }
        h1 { color: #2a4a7f; margin: 0; font-size: 1.5rem; text-transform: uppercase; letter-spacing: 2px; }
        .btn-logout { background: #222; color: #888; text-decoration: none; padding: 8px 15px; border: 1px solid #333; transition: 0.3s; }
        .btn-logout:hover { background: #5a1a1a; color: #fff; border-color: #ff3333; }
        .container { background-color: #0c0c0c; border: 1px solid #1a1a1a; border-radius: 4px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.8); max-width: 1200px; margin: 0 auto; }
        .log-line { padding: 8px 0; border-bottom: 1px dashed #1a1a1a; font-size: 14px; }
        .log-line:hover { background-color: #111; }
        .timestamp { color: #555; margin-right: 15px; }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1>Registros de Acceso Externo</h1>
          <a href="/admin/logout" class="btn-logout">Cerrar Sesión</a>
        </div>
        <div class="logs">
          ${logsHtml}
        </div>
      </div>
    </body>
    </html>
  `);
});

app.post("/admin/login", (req, res) => {
  const { password } = req.body;
  if (password === ADMIN_KEY) {
    res.cookie("auth_token", ADMIN_KEY, { maxAge: 24 * 60 * 60 * 1000, httpOnly: true });
    res.redirect("/admin");
  } else {
    res.send("<script>alert('Acceso Denegado'); window.location.href='/admin';</script>");
  }
});

app.get("/admin/logout", (req, res) => {
  res.clearCookie("auth_token");
  res.redirect("/admin");
});

// ─── WebSocket (Terminal Interactiva) ─────────────────────────
const wss = new WebSocket.Server({ server, path: "/ws" });

wss.on("connection", (ws, req) => {

  registrarAcceso(req, "Conexión WebSocket (Terminal)");

  const params   = new URL(req.url, "http://x").searchParams;
  const lang     = params.get("lang");
  const filename = params.get("file");
  const cfg      = RUNNERS[lang];

  if (!cfg || !filename) {
    ws.send("\x1b[31m[parametros invalidos]\x1b[0m\r\n");
    ws.close();
    return;
  }

  const absoluteRepo = path.resolve(REPO_PATH);
  const filePath = path.join(absoluteRepo, lang, filename);

  if (!fs.existsSync(filePath)) {
    ws.send(`\x1b[31mArchivo no encontrado: ${filePath}\x1b[0m\r\n`);
    ws.close();
    return;
  }

  const { cmd, args } = cfg.run(filePath);

  const term = pty.spawn(cmd, args, {
    name: "xterm-256color",
    cols: 120,
    rows: 40,
    cwd: absoluteRepo,
    env: { ...process.env, PYTHONUNBUFFERED: "1", FORCE_COLOR: "1", TERM: "xterm-256color" },
  });

  activeProcesses++;
  console.log(`[+] Executing: ${lang}/${filename} (Path: ${filePath})`);

  let idleTimer;
  const resetIdle = () => {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(() => {
      if (ws.readyState === WebSocket.OPEN)
        ws.send(`\r\n\x1b[33m[timeout por inactividad]\x1b[0m\r\n`);
      cleanup();
    }, IDLE_MS);
  };

  let cleaned = false;
  const cleanup = () => {
    if (cleaned) return;
    cleaned = true;
    clearTimeout(idleTimer);
    try { term.kill(); } catch (_) {}
    try { ws.close();  } catch (_) {}
    activeProcesses--;
  };

  resetIdle();

  term.onData((data) => {
    if (ws.readyState === WebSocket.OPEN) ws.send(data);
  });

  term.onExit(({ exitCode }) => {
    if (ws.readyState === WebSocket.OPEN) {
      const c = exitCode === 0 ? "\x1b[90m" : "\x1b[31m";
      ws.send(`\r\n${c}[proceso terminado — codigo ${exitCode}]\x1b[0m\r\n`);
    }
    cleanup();
  });

  ws.on("message", (raw) => {
    resetIdle();
    try {
      const msg = JSON.parse(raw.toString());
      if (msg.type === "resize") { term.resize(msg.cols, msg.rows); return; }
    } catch (_) {}
    try { term.write(raw.toString()); } catch (_) {}
  });

  ws.on("close", cleanup);
  ws.on("error", cleanup);
});

// ─── Start ────────────────────────────────────────────────────
// IMPORTANTE: 0.0.0.0 para que Railway sea visible externamente
server.listen(PORT, "0.0.0.0", () => {
  console.log(`🚀 Server online en puerto ${PORT}`);
  console.log(`📂 REPO_PATH: ${path.resolve(REPO_PATH)}`);
});