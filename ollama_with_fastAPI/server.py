from fastapi import FastAPI, Body
from ollama import Client

client = Client(
    host="http://localhost:11434",
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "ayan"}

@app.post("/chat")
def chat(
    message: str = Body(..., description="Hello, how are you?")
):
    response = client.chat(
        model="gemma:2b",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    return {"response": response["message"]["content"]}
