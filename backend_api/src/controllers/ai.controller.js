import { callAIService } from "../services/ai.service.js";

export const runTask = async (req, res) => {
  try {
    const result = await callAIService(req.body.task);
    res.json(result);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
};
