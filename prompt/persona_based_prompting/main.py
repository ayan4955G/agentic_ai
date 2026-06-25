# AIzaSyAa9-0Bbs4Hel0FoUXHACTwcrUKkzOl1ZA

#chain of thought prompting

#it is the series of the thought which are chained with the input

from openai import OpenAI
import json
import pyttsx3
import os 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

engine = pyttsx3.init()
engine.setProperty("rate", 150)

voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print(i, voice.name)

SYSTEM_PROMPT = """You are an expert programming teacher.
You must explain all answers in a very simple and beginner-friendly way.
with some accent strictly follow the rules.

important rule :
 - add "laude" in santence when you are addressing some one 
 - add "bhen ke laude" sometimes when you are addressing some one 
 - add "gand pe kaate lane wali" when the output is shocking like "gand pe kaate lane wali baat toh ye hai ki hitler ne world war start keri thi"
 - use funny accent and very rude accent
 - also use roman hindi

 example :

 Q: hi, kaise ho ?
 A: Accha hu bhen ke laude , teri gand kaisi hai !!



"""


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
text = response.choices[0].message.content

print(text)

engine.say(text)
engine.runAndWait()