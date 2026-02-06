import { useState } from "react";
import TaskInput from "./components/TaskInput";
import ResultView from "./components/ResultView";
import { runTask } from "./api/ai";

export default function App() {
  const [result, setResult] = useState(null);

  const handleRun = async (task) => {
    const res = await runTask(task);
    setResult(res);
  };

  return (
    <div>
      <h1>AI Ops Assistant</h1>
      <TaskInput onSubmit={handleRun} />
      {result && <ResultView result={result} />}
    </div>
  );
}
