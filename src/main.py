from fastapi import FastAPI
from data.mock_data import mock_data
from services.reservation_service import get_reservations

app = FastAPI(
    title="FastAPI Starter",
    description="Baseline FastAPI project.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return mock_data


@app.get("/reservations")
def read_reservations():
    return get_reservations()
