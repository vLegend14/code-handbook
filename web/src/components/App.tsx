import { useState, useEffect } from "react";
import type { Language, Module } from "../types";
import { API_URL } from "../config";
import Sidebar from "./Sidebar";
import TerminalPane from "./TerminalPane";
import Landing from "./Landing";

export default function App() {
  const [languages,    setLanguages]    = useState<Language[]>([]);
  const [activeLang,   setActiveLang]   = useState<string | null>(null);
  const [modules,      setModules]      = useState<Module[]>([]);
  const [activeModule, setActiveModule] = useState<Module | null>(null);
  const [loading,      setLoading]      = useState(true);
  const [error,        setError]        = useState<string | null>(null);

  // Cargar lenguajes al inicio
  useEffect(() => {
    fetch(`${API_URL}/api/languages`)
      .then((r) => r.json())
      .then((data: Language[]) => {
        setLanguages(data);
        if (data.length > 0) setActiveLang(data[0].id);
      })
      .catch(() => setError("No se puede conectar con el servidor"))
      .finally(() => setLoading(false));
  }, []);

  // Cargar módulos cuando cambia el lenguaje
  useEffect(() => {
    if (!activeLang) return;
    setActiveModule(null);
    setModules([]);
    fetch(`${API_URL}/api/modules/${activeLang}`)
      .then((r) => r.json())
      .then(setModules)
      .catch(console.error);
  }, [activeLang]);

  return (
    <div className="flex h-screen bg-base font-mono overflow-hidden">
      <Sidebar
        languages={languages}
        activeLang={activeLang}
        modules={modules}
        activeModule={activeModule}
        loading={loading}
        onSelectLang={setActiveLang}
        onSelectModule={setActiveModule}
      />

      <main className="flex flex-col flex-1 overflow-hidden">
        {error ? (
          <ErrorState message={error} />
        ) : activeModule && activeLang ? (
          <TerminalPane
            lang={activeLang}
            module={activeModule}
            key={`${activeLang}-${activeModule.name}`}
          />
        ) : (
          <Landing loading={loading} hasLangs={languages.length > 0} />
        )}
      </main>
    </div>
  );
}

function ErrorState({ message }: { message: string }) {
  return (
    <div className="flex flex-col items-center justify-center flex-1 gap-3 text-faint">
      <span className="text-2xl">⚠</span>
      <p className="text-sm">{message}</p>
      <p className="text-xs">¿Está el servidor corriendo?</p>
      <button
        onClick={() => window.location.reload()}
        className="mt-2 px-4 py-1.5 text-xs border border-border rounded hover:border-accent hover:text-accent transition-colors"
      >
        reintentar
      </button>
    </div>
  );
}
