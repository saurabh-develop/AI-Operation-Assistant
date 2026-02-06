import { useState } from "react";

export default function TaskInput({ onSubmit, loading }) {
  const [task, setTask] = useState("");

  return (
    <div className="flex gap-3">
      <input
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="Describe the task you want to run…"
        className="flex-1 rounded-xl bg-slate-800 border border-slate-700 px-4 py-3 text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        disabled={loading}
      />

      <button
        onClick={() => onSubmit(task)}
        disabled={!task || loading}
        className="rounded-xl bg-indigo-600 px-5 py-3 text-sm font-medium hover:bg-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed transition"
      >
        {loading ? "Running…" : "Run"}
      </button>
    </div>
  );
}
