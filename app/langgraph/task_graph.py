from app.agents.planner_agent import plan_task
from app.agents.search_agent import search_task
from app.agents.summarizer_agent import summarize_results

import asyncio

async def run_task_graph(goal):
    print(f"🧠 Starting plan for goal: {goal}")

    plan = plan_task(goal)
    print("✅ Plan Generated:", plan)

    combined_summary = []
    for task in plan:
        search_results = search_task(task)
        await asyncio.sleep(4)  # prevent hitting the 15/minute quota
        summary = summarize_results(search_results)
        combined_summary.append(f"{task} → {summary}")

    full_summary = "\n".join(combined_summary)

    return {
        "goal": goal,
        "plan": plan,
        "summary": full_summary
    }
