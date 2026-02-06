export default function ResultView({ result }) {
  return (
    <div className="rounded-xl bg-slate-800 border border-slate-700 p-4">
      <h2 className="text-sm font-semibold text-slate-300 mb-2">Result</h2>
      <pre className="text-sm text-emerald-400 overflow-x-auto whitespace-pre-wrap">
        {JSON.stringify(result, null, 2)}
      </pre>
    </div>
  );
}
