import express from "express";
import cors from "cors";
import aiRoutes from "./src/routes/ai.routes.js";
import dotenv from "dotenv";
dotenv.config();

const app = express();
app.use(cors({ origin: "http://localhost:5173" }));
app.use(express.json());
app.use("/api/ai", aiRoutes);

export default app;

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => console.log(`Node API running on ${PORT}`));
