import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class GeminiAPI:
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    async def gemini_response(self, prompt):  
            response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction="your instructions",
                        max_output_tokens=100,
                        temperature=0.5,
            )
            )
            return response.text