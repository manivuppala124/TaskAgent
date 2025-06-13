from app.utils.gemini import gemini_prompt

def plan_task(goal):
    prompt = f"""You are a smart planner agent. Break down the following goal into 3-5 clear subtasks:\nGoal: {goal}\nPlease return only bullet points."""
    response = gemini_prompt(prompt)
    # Convert the bullet points to a Python list
    tasks = [line.strip("-•* ").strip() for line in response.splitlines() if line.strip()]
    return tasks
