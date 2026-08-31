from fastapi import FastAPI

from routers.inventory import router as inventory_router

app = FastAPI(
    title="Retail Inventory Management System",
    description=(
        "Inventory management API for Cornerline Home Goods. "
        "Supports catalog management with real-time quantity tracking."
    ),
    version="0.1.0",
)

app.include_router(inventory_router)


@app.get("/", tags=["Health"])
def read_root() -> dict[str, str]:
    return {"message": "Retail Inventory Management System API"}
