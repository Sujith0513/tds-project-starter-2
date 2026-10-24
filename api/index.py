import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

AIPIPE_URL = "https://aipipe.org/openai/v1/chat/completions"
MODEL = os.getenv("MODEL", "gpt-4.1-nano")

app = FastAPI(title="TDS Project Starter")

# Allow any origin so graders and browsers can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SolveRequest(BaseModel):
    question: str


class SolveResponse(BaseModel):
    answer: str


def ask_llm(prompt: str) -> str:
    token = os.getenv("AIPIPE_TOKEN")
    if not token:
        # No token set: return an echo so the endpoint still works for testing
        return f"You asked: {prompt}"
    resp = httpx.post(
        AIPIPE_URL,
        headers={"Authorization": f"Bearer {token}"},
        json={"model": MODEL, "messages": [{"role": "user", "content": prompt}]},
        timeout=30,
    )
    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail=f"LLM error: {resp.text[:200]}")
    return resp.json()["choices"][0]["message"]["content"]


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/api/solve", response_model=SolveResponse)
def solve(req: SolveRequest):
    # TODO: replace with your project logic
    return SolveResponse(answer=ask_llm(req.question))
