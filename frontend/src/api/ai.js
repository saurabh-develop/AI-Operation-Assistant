import axios from "axios";

export const runTask = async (task) => {
  const res = await axios.post("http://localhost:5001/api/ai/run-task", {
    task,
  });
  return res.data;
};
