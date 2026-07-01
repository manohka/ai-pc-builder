from openai import OpenAI

from app.core.config import settings


class LlmClient:

    MODEL = "gpt-5"

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate(self, prompt: str):

        response = self.client.responses.create(
            model=self.MODEL,
            input=prompt
        )

        return response.output_text
