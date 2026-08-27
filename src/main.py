from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Starter",
    description="Baseline FastAPI project.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}
