from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,  # Your Claude API key
    base_url="https://api.anthropic.com/v1/"  # the Claude API endpoint
)

response = client.chat.completions.create(
    model="claude-sonnet-4-5", # Anthropic model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"}
    ],
)

print(response.choices[0].message.content)