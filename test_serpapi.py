from app.langgraph.task_graph import run_task_graph

goal = "Write a plan to build a personal AI assistant"
output = run_task_graph(goal)
print(output)
