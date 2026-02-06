import { useState } from "react";
import TaskInput from "./components/TaskInput";
import ResultView from "./components/ResultView";
import { runTask } from "./api/ai";
import ErrorView from "./components/ErrorView";

export default function App() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleRun = async (task) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await runTask(task);
      setResult(res);
    } catch (err) {
      setError(err?.message || "Something went wrong while running the task.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-linear-to-br from-slate-900 via-slate-800 to-slate-900 text-white flex items-center justify-center p-6">
      <div className="w-full max-w-3xl bg-slate-900/70 backdrop-blur rounded-2xl shadow-xl border border-slate-700 p-6 space-y-6">
        <h1 className="text-2xl font-semibold tracking-tight text-center">
          🤖 AI Ops Assistant
        </h1>

        <TaskInput onSubmit={handleRun} loading={loading} />

        {error && <ErrorView error={error} />}
        {result && <ResultView result={result} />}
      </div>
    </div>
  );
}
