from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.orchestrator import Orchestrator
import traceback

app = FastAPI(title="AI Operation Assistant")


orchestrator = Orchestrator()


class TaskRequest(BaseModel):
    task: str

class TaskResponse(BaseModel):
    result: dict

@app.post("/run-task", response_model=TaskResponse)
def run_task(req: TaskRequest):
    try:
        result = orchestrator.run(req.task)
        return {"result": result}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))