import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt: str , model: str = "llama3.2:3b") -> str:
    response = requests.post(OLLAMA_URL, json = {
        "model": model,
        "prompt": prompt,
        "stream": False

    })

    response.raise_for_status()
    return response.json()["response"]