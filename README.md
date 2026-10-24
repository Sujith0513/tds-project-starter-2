# TDS Project Starter

A ready-to-run FastAPI skeleton for a TDS project. It has the folder structure, one API endpoint, CORS, an AI Pipe LLM helper, and deploy files for Render, Vercel and Docker. Add your own logic in `api/index.py`.

If `AIPIPE_TOKEN` is set in `.env`, `/api/solve` sends the question to an LLM through AI Pipe. Without a token it just echoes the question, so you can test it for free.

## Run locally

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn api.index:app --reload
```

Open http://127.0.0.1:8000 and you should see `{"status": "ok"}`.

## Test the endpoint

```bash
curl -X POST http://127.0.0.1:8000/api/solve -H "Content-Type: application/json" -d '{"question": "hello"}'
```

Expected reply: `{"answer": "You asked: hello"}`

## Deploy

**Render:** New > Blueprint > pick this repo. It reads `render.yaml`. Add `AIPIPE_TOKEN` in the Environment tab.

**Vercel:** Import this repo at vercel.com/new. Add `AIPIPE_TOKEN` under Settings > Environment Variables.

**Docker:**

```bash
docker build -t tds-starter .
docker run -p 8000:8000 --env-file .env tds-starter
```

## Files

| File | Purpose |
|---|---|
| `api/index.py` | The API. Put your logic in `solve()` |
| `requirements.txt` | Python packages |
| `.env.example` | Template for secrets. Copy to `.env`, never commit `.env` |
| `Dockerfile` | Container build |
| `render.yaml` | Render deploy config |
| `vercel.json` | Vercel deploy config |
| `LICENSE` | MIT license |
