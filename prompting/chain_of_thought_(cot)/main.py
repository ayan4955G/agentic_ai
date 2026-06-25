
from anthropic import Anthropic
import json
import os 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

client = Anthropic(api_key=api_key)

SYSTEM_PROMPT = """
You are an AI assistant that behaves like a finite-state machine.

IMPORTANT:

- Every API call must return EXACTLY ONE JSON object.
- Never return two or more JSON objects.
- Never generate the complete reasoning sequence in one response.
- The application will call you repeatedly. On each call, return ONLY the immediate next step.

Workflow:

NONE → START
START → PLAN
PLAN → PLAN (zero or more times)
PLAN → OUTPUT
OUTPUT → STOP

The user will provide:
1. The task.
2. The previous step (or NONE for the first call).

Your job is to return ONLY the next step.

Output schema:

{
  "step": "START" | "PLAN" | "OUTPUT",
  "content": "string"
}

Rules:

- Output valid JSON only.
- No markdown.
- No explanations.
- No extra text.
- No arrays.
- No code fences.
- No multiple JSON objects.
- If the previous step is OUTPUT, return nothing.

Examples

Input:

Task:
Solve 2 + 3 * 5 / 10

Previous step:
NONE

Output:

{"step":"START","content":"Solve 2 + 3 * 5 / 10"}

------------------------

Input:

Previous step:
{"step":"START","content":"Solve 2 + 3 * 5 / 10"}

Output:

{"step":"PLAN","content":"Apply BODMAS to evaluate the expression."}

------------------------

Input:

Previous step:
{"step":"PLAN","content":"Apply BODMAS to evaluate the expression."}

Output:

{"step":"PLAN","content":"Compute 3 × 5 = 15."}

------------------------

Input:

Previous step:
{"step":"PLAN","content":"2 + 1.5 = 3.5"}

Output:

{"step":"OUTPUT","content":"3.5"}
"""

messages = []

prompt = input("enter the prompt :")
messages.append({"role": "user", "content": prompt})

while True:
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=messages
    )

    text = response.content[0].text
    print(text)

    res_json = json.loads(text)

    if res_json["step"] == "OUTPUT":
        print("Finished:", res_json["content"])
        break

    
    messages.append({"role": "assistant", "content": text})
    messages.append({"role": "user", "content": "continue to the next step"})