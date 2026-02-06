export default function ErrorView({ error }) {
  return (
    <div className="rounded-xl bg-red-500/10 border border-red-500/30 p-4">
      <h2 className="text-sm font-semibold text-red-400 mb-1">Error</h2>
      <p className="text-sm text-red-300">{error}</p>
    </div>
  );
}
