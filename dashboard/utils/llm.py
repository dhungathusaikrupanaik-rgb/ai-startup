# utils/llm.py
import os
import requests
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv("LLM_MODE", "local")  # "local" or "api"
LOCAL_ENDPOINT = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:8080/v1/chat/completions")
REMOTE_ENDPOINT = os.getenv("REMOTE_LLM_URL", "")
REMOTE_API_KEY = os.getenv("REMOTE_LLM_KEY", "")

def call_model(prompt: str, system: str = None, max_tokens: int = 512) -> str:
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    if MODE == "local":
        payload = {"model": "local-model", "messages": messages, "max_tokens": max_tokens}
        try:
            r = requests.post(LOCAL_ENDPOINT, json=payload, timeout=60)
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"[llm error] {e}"
    else:
        headers = {"Authorization": f"Bearer {REMOTE_API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "llama-3.3-70b-versatile", "messages": messages, "max_tokens": max_tokens}
        try:
            r = requests.post(REMOTE_ENDPOINT, json=payload, headers=headers, timeout=60)
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"[llm error] {e}"
