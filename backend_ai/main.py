from dotenv import load_dotenv
load_dotenv()
from core.errors import AIError
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from core.orchestrator import Orchestrator
import traceback

app = FastAPI(title="AI Operation Assistant")


@app.exception_handler(AIError)
async def ai_error_handler(request: Request, exc: AIError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details
            }
        }
    )

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "Something went wrong"
            }
        }
    )

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