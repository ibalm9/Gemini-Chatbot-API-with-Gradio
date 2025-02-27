import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiModel:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('models/gemini-2.0-flash-lite')
    
    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
