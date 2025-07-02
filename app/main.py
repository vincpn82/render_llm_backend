from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Prompt(BaseModel):
    prompt: str

@app.post("/chat")
def chat(data: Prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": data.prompt}]
    )
    return {"response": completion.choices[0].message["content"]}
