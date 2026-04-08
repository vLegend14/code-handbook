/**
 * code-handbook — server.js
 */

const express   = require("express");
const http      = require("http");
const WebSocket = require("ws");
const pty       = require("node-pty");
const path      = require("path");
const fs        = require("fs");
const cors      = require("cors");
const { execSync } = require("child_process");

// ─── Config ───────────────────────────────────────────────────
const PORT         = process.env.PORT      || 8080;
const REPO_PATH    = process.env.REPO_PATH || '.';
const MAX_PROCS    = parseInt(process.env.MAX_PROCS || "10");
const IDLE_MS      = parseInt(process.env.IDLE_MS   || "300000");

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

// ─── Express ──────────────────────────────────────────────────
const app    = express();
const server = http.createServer(app);

const allowedOrigins = [
  "https://vlegend14.github.io",
  "http://localhost:4321",
  "http://localhost:3000"
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

// ─── Endpoints ────────────────────────────────────────────────

app.get("/health", (_, res) => res.json({ ok: true, active: activeProcesses }));

// Endpoint de Debug
app.get("/debug-env", (req, res) => {
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

// ─── WebSocket (Terminal Interactiva) ─────────────────────────
const wss = new WebSocket.Server({ server, path: "/ws" });

wss.on("connection", (ws, req) => {
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