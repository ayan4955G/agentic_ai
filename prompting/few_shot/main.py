import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.anthropic.com/v1/",
)

SYSTEM_PROMPT = """Translate English to French.

                Example 1:
                English: Hello
                French: Bonjour

                Example 2:
                English: Thank you
                French: Merci

                Now translate:
                English: Good night"""

response = client.chat.completions.create(
    model="claude-opus-4-8",  
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)

print(response.choices[0].message.content)