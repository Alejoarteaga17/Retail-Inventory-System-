from fastapi import FastAPI

from dependencies import inventory_service
from routers.inventory import router as inventory_router

app = FastAPI(
    title="Retail Inventory Management System",
    description=(
        "API for Cornerline Home Goods inventory catalog management. "
        "Supports creating, viewing, updating, and deactivating inventory items."
    ),
    version="0.1.0",
)


@app.get("/", tags=["Health"])
def read_root() -> dict[str, str]:
    return {"message": "Retail Inventory Management System API"}


app.include_router(inventory_router)

__all__ = ["app", "inventory_service"]
