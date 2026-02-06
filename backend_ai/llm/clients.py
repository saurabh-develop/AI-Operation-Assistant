import os
from google import genai

class LLMClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=api_key)

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        prompt = f"""
{system_prompt}

{user_prompt}

IMPORTANT:
- Output ONLY valid JSON
- No markdown
- No explanations
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        start = text.find("{")
        end = text.rfind("}") + 1

        if start == -1 or end == -1:
            raise ValueError(f"Invalid Gemini response: {text}")

        return text[start:end]
