import { useEffect, useRef, useState, useCallback } from "react";
import type { Module } from "../types";
import { WS_URL } from "../config";

interface Props {
  lang:   string;
  module: Module;
}

type Status = "connecting" | "running" | "done" | "error";

export default function TerminalPane({ lang, module }: Props) {
  const containerRef = useRef<HTMLDivElement>(null);
  const termRef      = useRef<any>(null);
  const fitRef       = useRef<any>(null);
  const wsRef        = useRef<WebSocket | null>(null);
  const [status, setStatus] = useState<Status>("connecting");

  const connect = useCallback(() => {
    // Limpiar sesión anterior
    if (wsRef.current) wsRef.current.close();
    termRef.current?.clear();
    termRef.current?.reset();

    setStatus("connecting");

    const url = `${WS_URL}/ws?lang=${lang}&file=${encodeURIComponent(module.name)}`;
    const ws  = new WebSocket(url);
    wsRef.current = ws;

    ws.onopen = () => {
      setStatus("running");
      // Enviar tamaño del terminal
      if (termRef.current) {
        const { cols, rows } = termRef.current;
        ws.send(JSON.stringify({ type: "resize", cols, rows }));
      }
    };

    ws.onmessage = (e) => {
      termRef.current?.write(e.data);
    };

    ws.onclose = () => {
      setStatus((s) => s === "error" ? "error" : "done");
    };

    ws.onerror = () => {
      setStatus("error");
      termRef.current?.writeln("\r\n\x1b[31m[error de conexión]\x1b[0m");
    };
  }, [lang, module.name]);

  // Montar xterm una sola vez
  useEffect(() => {
    if (!containerRef.current) return;

    // Importar xterm dinámicamente (no existe en SSR de Astro)
    Promise.all([
      import("@xterm/xterm"),
      import("@xterm/addon-fit"),
      import("@xterm/addon-web-links"),
    ]).then(([{ Terminal }, { FitAddon }, { WebLinksAddon }]) => {
      const term = new Terminal({
        theme: {
          background:   "#0d0d12",
          foreground:   "#e2e2e8",
          cursor:       "#7c6af7",
          cursorAccent: "#0d0d12",
          black:        "#1e1e28",
          red:          "#f05e7e",
          green:        "#4fc3a1",
          yellow:       "#f5c97a",
          blue:         "#7c6af7",
          magenta:      "#c792ea",
          cyan:         "#89ddff",
          white:        "#e2e2e8",
          brightBlack:  "#55556a",
          brightWhite:  "#ffffff",
        },
        fontSize:    14,
        fontFamily:  "'Fira Code', 'Cascadia Code', monospace",
        lineHeight:  1.5,
        cursorBlink: true,
        scrollback:  5000,
        allowTransparency: true,
      });

      const fit   = new FitAddon();
      const links = new WebLinksAddon();

      term.loadAddon(fit);
      term.loadAddon(links);
      term.open(containerRef.current!);

      termRef.current = term;
      fitRef.current  = fit;

      fit.fit();

      // Teclas → WebSocket
      term.onData((data) => {
        if (wsRef.current?.readyState === WebSocket.OPEN) {
          wsRef.current.send(data);
        }
      });

      // Resize
      const ro = new ResizeObserver(() => {
        try {
          fit.fit();
          if (wsRef.current?.readyState === WebSocket.OPEN) {
            wsRef.current.send(JSON.stringify({ type: "resize", cols: term.cols, rows: term.rows }));
          }
        } catch (_) {}
      });
      ro.observe(containerRef.current!);

      connect();

      return () => {
        ro.disconnect();
        term.dispose();
      };
    });

    return () => {
      wsRef.current?.close();
    };
  // Solo se monta una vez
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Cuando cambia el módulo (key cambia en App.tsx → remonta el componente)
  useEffect(() => {
    if (termRef.current) connect();
  }, [connect]);

  // F5 global para re-ejecutar
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === "F5") { e.preventDefault(); connect(); }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [connect]);

  const STATUS_STYLES: Record<Status, string> = {
    connecting: "bg-yellow-500/20 text-yellow-400",
    running:    "bg-green/20 text-green",
    done:       "bg-faint/20 text-faint",
    error:      "bg-red-500/20 text-red-400",
  };
  const STATUS_LABEL: Record<Status, string> = {
    connecting: "conectando",
    running:    "ejecutando",
    done:       "terminado",
    error:      "error",
  };

  return (
    <div className="flex flex-col flex-1 overflow-hidden">

      {/* Topbar */}
      <div className="flex items-center gap-3 px-5 h-11 border-b border-border bg-surface shrink-0">
        {/* Status dot */}
        <span className={`inline-flex items-center gap-1.5 text-[10px] px-2 py-0.5 rounded-full font-medium ${STATUS_STYLES[status]}`}>
          <span className={`w-1.5 h-1.5 rounded-full inline-block ${status === "running" ? "animate-pulse" : ""}`}
            style={{ background: "currentColor" }} />
          {STATUS_LABEL[status]}
        </span>

        {/* Breadcrumb */}
        <span className="text-xs text-faint flex-1 truncate">
          <span className="text-muted">{lang}</span>
          <span className="mx-1">/</span>
          <span className="text-white">{module.title}</span>
        </span>

        {/* Actions */}
        <div className="flex items-center gap-2">
          <button
            onClick={() => { termRef.current?.clear(); }}
            className="text-[10px] text-faint hover:text-muted transition-colors px-2 py-1 rounded border border-transparent hover:border-border"
          >
            limpiar
          </button>
          <button
            onClick={() => { wsRef.current?.close(); setStatus("done"); }}
            className="text-[10px] text-faint hover:text-red-400 transition-colors px-2 py-1 rounded border border-transparent hover:border-border"
            disabled={status !== "running"}
          >
            detener
          </button>
          <button
            onClick={connect}
            disabled={status === "connecting" || status === "running"}
            className="text-[10px] px-3 py-1 bg-accent text-white rounded hover:opacity-80 transition-opacity disabled:opacity-30 disabled:cursor-not-allowed"
          >
            ▶ ejecutar
          </button>
        </div>
      </div>

      {/* Terminal */}
      <div className="flex-1 bg-[#0d0d12] overflow-hidden p-2">
        <div ref={containerRef} className="w-full h-full" />
      </div>

    </div>
  );
}
