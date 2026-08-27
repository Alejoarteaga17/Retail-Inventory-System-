from fastapi import FastAPI

from api.errors import register_exception_handlers
from api.routers import insights, items, movements
from data.mock_data import mock_data
from services.reservation_service import get_reservations

API_PREFIX = "/api/v1"

app = FastAPI(
    title="Retail Inventory Management System",
    description=(
        "Inventory API for Cornerline Home Goods: item catalog, stock "
        "movements and low-stock insights. Data is served from an in-memory "
        "mock store, so it resets on every restart."
    ),
    version="0.2.0",
)

register_exception_handlers(app)

app.include_router(items.router, prefix=API_PREFIX)
app.include_router(movements.router, prefix=API_PREFIX)
app.include_router(insights.router, prefix=API_PREFIX)


@app.get("/health", tags=["Meta"], summary="Liveness probe")
def health():
    return {"status": "ok"}


@app.get("/")
def read_root():
    return mock_data


@app.get("/reservations")
def read_reservations():
    return get_reservations()
