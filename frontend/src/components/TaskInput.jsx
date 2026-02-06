import { useState } from "react";

export default function TaskInput({ onSubmit }) {
  const [task, setTask] = useState("");
  return (
    <div>
      <input
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="Enter task"
      />
      <button onClick={() => onSubmit(task)}>Run</button>
    </div>
  );
}
