import type { Language, Module } from "../types";

const LANG_META: Record<string, { color: string; label: string }> = {
  python:     { color: "#4b8bbe", label: "Python"     },
  javascript: { color: "#f0db4f", label: "JavaScript" },
  typescript: { color: "#3178c6", label: "TypeScript" },
  cpp:        { color: "#659ad2", label: "C++"        },
  java:       { color: "#ed8b00", label: "Java"       },
};

interface Props {
  languages:    Language[];
  activeLang:   string | null;
  modules:      Module[];
  activeModule: Module | null;
  loading:      boolean;
  onSelectLang:   (lang: string) => void;
  onSelectModule: (mod: Module) => void;
}

export default function Sidebar({
  languages, activeLang, modules, activeModule, loading,
  onSelectLang, onSelectModule,
}: Props) {
  return (
    <aside className="flex flex-col w-64 border-r border-border bg-surface shrink-0 overflow-hidden">

      {/* Header */}
      <div className="px-5 py-4 border-b border-border">
        <h1 className="text-sm font-medium text-white tracking-tight">
          code-handbook
        </h1>
        <p className="text-xs text-faint mt-0.5">apuntes interactivos</p>
      </div>

      {/* Language tabs */}
      <div className="flex flex-wrap gap-1 px-3 pt-3 pb-0">
        {loading ? (
          <div className="text-xs text-faint px-2 py-1">cargando...</div>
        ) : (
          languages.map((lang) => {
            const meta   = LANG_META[lang.id] ?? { color: "#888", label: lang.id };
            const active = lang.id === activeLang;
            return (
              <button
                key={lang.id}
                onClick={() => onSelectLang(lang.id)}
                className={`
                  flex items-center gap-1.5 px-2.5 py-1 text-xs rounded
                  border transition-all duration-150
                  ${active
                    ? "border-border bg-raised text-white"
                    : "border-transparent text-muted hover:text-white hover:bg-raised"
                  }
                `}
              >
                <span
                  className="inline-block w-1.5 h-1.5 rounded-full shrink-0"
                  style={{ background: meta.color }}
                />
                {meta.label}
              </button>
            );
          })
        )}
      </div>

      {/* Divider */}
      <div className="mx-3 mt-3 border-t border-border" />

      {/* Module list */}
      <div className="flex-1 overflow-y-auto py-2">
        {modules.length === 0 ? (
          <p className="text-xs text-faint text-center mt-6">
            {activeLang ? "No hay módulos" : "Selecciona un lenguaje"}
          </p>
        ) : (
          modules.map((mod) => {
            const active = mod.name === activeModule?.name;
            const [num, ...rest] = mod.title.split(" · ");
            return (
              <button
                key={mod.name}
                onClick={() => onSelectModule(mod)}
                className={`
                  w-full flex items-center gap-3 px-5 py-2.5 text-left
                  border-l-2 transition-all duration-100
                  ${active
                    ? "border-accent bg-raised text-white"
                    : "border-transparent text-muted hover:bg-raised hover:text-white"
                  }
                `}
              >
                <span className="text-[10px] text-faint w-5 shrink-0 font-medium">
                  {num}
                </span>
                <span className="text-xs truncate">
                  {rest.join(" · ") || mod.name}
                </span>
              </button>
            );
          })
        )}
      </div>

      {/* Footer */}
      <div className="px-5 py-3 border-t border-border">
        <p className="text-[10px] text-faint">
          <kbd className="bg-raised border border-border rounded px-1 py-0.5 text-[9px]">F5</kbd>
          {" "}re-ejecutar  ·  {" "}
          <kbd className="bg-raised border border-border rounded px-1 py-0.5 text-[9px]">Ctrl+C</kbd>
          {" "}interrumpir
        </p>
      </div>

    </aside>
  );
}
