from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
import uvicorn
import asyncio
from nlp_processor import execute_nlp 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

model = OllamaLLM(model="gemma:2b")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    user_message = request.message

    nlp_response = execute_nlp(user_message)
    if nlp_response:
        return {"response": nlp_response, "source": "Avatar"}

    prompt = f"Jawab dengan singkat: {user_message}"
    ai_response = await asyncio.to_thread(model.invoke, input=prompt)
    
    return {"response": ai_response, "source": "Avatar"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
