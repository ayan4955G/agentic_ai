# AIzaSyAa9-0Bbs4Hel0FoUXHACTwcrUKkzOl1ZA

#zero shot prompting 

#zero prompting basically means directly giving the instruction to the model for example

from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")


SYSTEM_PROMPT = "you should only and only ans the coding related questions. Do not ans anything " \
"else. Your name is Ayan Shaikh. If user asks something other than coding , just say sorry"

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

user_input = input("enter the input prompt: ")

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": user_input
        }
    ]
)

print(response.choices[0].message.content)