import os 
import google.generativeai as genai

class LLMClient:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def chat(self, system_prompt: str, user_promt:str)->str:
        prompt = f"""
{system_prompt}

{user_promt}
"""
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0,
                "response_mime_type": "application/json"
            }
        )
        return response.text.strip()