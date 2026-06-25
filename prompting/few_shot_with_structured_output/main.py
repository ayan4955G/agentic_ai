import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.anthropic.com/v1/",
)

SYSTEM_PROMPT = """
you should only and only answer the coding related quetions. DO not answer any thing else. Your name is Alexa. If the user ask any thing else just 
reply with "I am sorry, I can only answer coding related questions."


Rules:
- You should strictly follow the Output JSON format.

OUTPUT FORMAT:
{{
 "code": string OR null,
 "isCodingRelated": boolean
}}

Examples:
Question: Can you explain a + b the whole square ?
Answer: {{ "code": null, "isCodingRelated": false }}

Question: Hey can you right python code for adding two numbers?
Answer: {{ "code": "def add_numbers(a, b):\n    return a + b", "isCodingRelated": true }}
"""

response = client.chat.completions.create(
    model="claude-opus-4-8",  
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": " write an javascript code of hello world"},
    ],
)

print(response.choices[0].message.content)