from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from exceptions.authorization import InsufficientRoleError
from routers.alerts import router as alerts_router
from routers.inventory import router as inventory_router

app = FastAPI(
    title="Retail Inventory Management System",
    description=(
        "Inventory management API for Cornerline Home Goods. "
        "Supports catalog management with real-time quantity tracking "
        "and low-stock alerting."
    ),
    version="0.2.0",
)

app.include_router(inventory_router)
app.include_router(alerts_router)


@app.exception_handler(InsufficientRoleError)
def handle_insufficient_role(_: Request, exc: InsufficientRoleError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": str(exc)})


@app.get("/", tags=["Health"])
def read_root() -> dict[str, str]:
    return {"message": "Retail Inventory Management System API"}
