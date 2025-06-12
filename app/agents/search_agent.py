from app.tools.search_tool import search_query

def search_task(task: str):
    print(f"[Search Agent] 🔍 Searching for: {task}")
    results = search_query(task)
    return results
