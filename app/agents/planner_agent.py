from app.utils.gemini import gemini_prompt

def plan_task(goal):
    prompt = f"""
You are a smart planner agent. Break down the following goal into 3-5 clear subtasks:
Goal: {goal}
Please return only bullet points.
"""
    return gemini_prompt(prompt)
