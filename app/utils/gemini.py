import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def gemini_prompt(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        if "ResourceExhausted" in str(e):
            return "⚠️ Gemini API quota exceeded. Please wait and try again in a minute or upgrade your quota."
        raise
