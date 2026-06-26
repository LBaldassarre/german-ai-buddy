import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class GeminiAPI:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    async def gemini_response(self, prompt):  
            response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction="your instructions",
                        max_output_tokens=512,
                        temperature=0.5,
                        thinking_config=types.ThinkingConfig(
                            thinking_budget=0
                        )
            )
            )
            print(response)
            return response.text