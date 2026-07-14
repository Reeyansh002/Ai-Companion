from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from llm import ask_llm
from tts import speak

app = FastAPI()

# Allows the browser (running on a different port) to talk to this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    reply_text = ask_llm(req.message)
    audio_path = speak(reply_text)
    return {"reply": reply_text, "audio_url": "/audio"}

@app.get("/audio")
def get_audio():
    return FileResponse("output.wav", media_type="audio/wav")