interface Props {
  loading:  boolean;
  hasLangs: boolean;
}

export default function Landing({ loading, hasLangs }: Props) {
  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center flex-1 gap-3 text-faint">
        <div className="w-5 h-5 border-2 border-border border-t-accent rounded-full animate-spin" />
        <p className="text-xs">conectando con el servidor...</p>
      </div>
    );
  }

  if (!hasLangs) {
    return (
      <div className="flex flex-col items-center justify-center flex-1 gap-2 text-faint">
        <p className="text-sm">No se encontraron lenguajes</p>
        <p className="text-xs">
          Asegúrate de que <code className="text-muted bg-raised px-1 py-0.5 rounded">REPO_PATH</code> apunta al repo correcto
        </p>
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center justify-center flex-1 gap-4 text-faint select-none">
      <pre className="text-[10px] leading-tight text-faint/40">{`
  ╔═══════════════════════╗
  ║   code-handbook       ║
  ║   apuntes             ║
  ╚═══════════════════════╝`}
      </pre>
      <div className="flex flex-col items-center gap-1">
        <p className="text-sm text-muted">Selecciona un módulo</p>
        <p className="text-xs">
          Elige un lenguaje y un archivo del panel izquierdo
        </p>
      </div>
      <div className="flex gap-6 text-[10px] mt-2">
        <span>
          <kbd className="bg-raised border border-border rounded px-1.5 py-0.5 text-muted">Enter</kbd>
          {" "}continuar pausas
        </span>
        <span>
          <kbd className="bg-raised border border-border rounded px-1.5 py-0.5 text-muted">Ctrl+C</kbd>
          {" "}interrumpir
        </span>
        <span>
          <kbd className="bg-raised border border-border rounded px-1.5 py-0.5 text-muted">F5</kbd>
          {" "}re-ejecutar
        </span>
      </div>
    </div>
  );
}
