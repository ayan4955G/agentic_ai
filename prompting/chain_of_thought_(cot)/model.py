import anthropic
import os 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

client = anthropic.Anthropic(
    api_key=api_key
)

models = client.roles.list()

for model in roles.data:
    print(model.id)