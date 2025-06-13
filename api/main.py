from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import traceback
from app.langgraph.task_graph import run_task_graph
from fastapi.middleware.cors import CORSMiddleware

# ✅ Step 1: Define the app first
app = FastAPI()

# ✅ Step 2: Add middleware after app is defined
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your Streamlit frontend for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Step 3: Root route (optional but useful for debugging)
@app.get("/")
def read_root():
    return {"message": "✅ TaskAgent backend is running!"}

# ✅ Step 4: Pydantic model for request
class TaskRequest(BaseModel):
    goal: str

# ✅ Step 5: API endpoint
@app.post("/plan-task/")
async def plan_task_api(req: TaskRequest):
    try:
        return await run_task_graph(req.goal)
    except Exception as e:
        print("❌ ERROR TRACEBACK ❌")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {str(e)}")
