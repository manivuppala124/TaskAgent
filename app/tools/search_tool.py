from duckduckgo_search import DDGS

def search_query(query: str, max_results: int = 5):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            return [
                f"{r.get('title', '')} - {r.get('body', '')} ({r.get('href', '')})"
                for r in results
            ]
    except Exception as e:
        return [f"Search failed: {str(e)}"]
