from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import traceback
from app.langgraph.task_graph import run_task_graph
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

class TaskRequest(BaseModel):
    goal: str

@app.post("/plan-task/")
async def plan_task_api(req: TaskRequest):
    try:
        return await run_task_graph(req.goal)
    except Exception as e:
        print("❌ ERROR TRACEBACK ❌")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {str(e)}")
