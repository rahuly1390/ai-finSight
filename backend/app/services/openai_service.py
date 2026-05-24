from openai import OpenAI

from app.config.settings import settings
from app.prompts.financial_prompt import (
    FINANCIAL_SYSTEM_PROMPT,
)


class OpenAIService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def ask(self, query: str):

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": FINANCIAL_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content


openai_service = OpenAIService()