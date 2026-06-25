import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.anthropic.com/v1/",
)

response = client.chat.completions.create(
    model="claude-opus-4-8",  
    messages=[
        {"role": "system", "content": "Translate English to French. Example English: Hello, how are you? French: Bonjour, comment ça va?"},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)

print(response.choices[0].message.content)