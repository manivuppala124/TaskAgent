from app.agents.planner_agent import plan_task
from app.agents.search_agent import search_task
from app.agents.summarizer_agent import summarize_results
from app.tools.storage_tool import log_task

def run_task_graph(goal):
    print(f"🧠 Starting plan for goal: {goal}")
    
    plan = plan_task(goal)
    print("✅ Plan Generated:", plan)

    search_results = search_task(goal)
    print("🔍 Search Results:", search_results)

    summary = summarize_results(search_results)
    print("📋 Summary Created:", summary)

    log_task(goal, summary)

    return {
        "goal": goal,
        "plan": plan,
        "summary": summary
    }
