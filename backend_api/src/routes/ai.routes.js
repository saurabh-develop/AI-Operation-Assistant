import express from "express";
import { runTask } from "../controllers/ai.controller.js";

const router = express.Router();
router.post("/run-task", runTask);
export default router;
