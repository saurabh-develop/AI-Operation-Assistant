from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.planner import PlannerAgent

app = FastAPI(title="AI Operations Assistant")

planner = PlannerAgent()

class TaskRequest(BaseModel):
    task:str

class PlanResponse(BaseModel):
    plan: dict

@app.post("/plan", response_model=PlanResponse)

def generate_plan(req: TaskRequest):
    try:
        plan = planner.create_plan(req.task)
        return {"plan": plan}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))