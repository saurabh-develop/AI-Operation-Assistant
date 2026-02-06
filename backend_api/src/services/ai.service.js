import axios from "axios";

export const callAIService = async (task) => {
  const response = await axios.post("http://localhost:8000/run-task", { task });
  return response.data;
};
