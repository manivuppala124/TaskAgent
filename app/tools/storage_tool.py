import json
from datetime import datetime
import os

def log_task(goal, summary):
    os.makedirs("app/data", exist_ok=True)
    log_entry = {
        "timestamp": str(datetime.now()),
        "goal": goal,
        "summary": summary
    }
    with open("app/data/task_logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
