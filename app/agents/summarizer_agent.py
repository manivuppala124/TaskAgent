from app.utils.gemini import gemini_prompt

def summarize_results(results):
    prompt = "Summarize the following search results into 5 bullet points:\n\n"
    for i, result in enumerate(results, 1):
        prompt += f"{i}. {result}\n"
    return gemini_prompt(prompt)
