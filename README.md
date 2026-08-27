# FastAPI Starter

Baseline FastAPI project with a single root endpoint. Fork it and build from here.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn src/main:app --reload
```

## Endpoints

| Method | Path | Response                     |
| ------ | ---- | ---------------------------- |
| GET    | `/`  | `{"message": "Hello World"}` |

Interactive docs: http://127.0.0.1:8000/docs
