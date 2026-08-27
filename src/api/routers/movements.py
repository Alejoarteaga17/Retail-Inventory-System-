"""Stock movement endpoints (stock-in, stock-out, adjustments, history)."""

from fastapi import APIRouter, status

from api.dependencies import ActorDep, StockDep
from api.schemas import ErrorRead, MovementCreate, MovementRead

router = APIRouter(tags=["Stock movements"])


@router.post(
    "/items/{item_id}/movements",
    response_model=MovementRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        403: {"model": ErrorRead, "description": "Role may not adjust stock."},
        404: {"model": ErrorRead, "description": "Unknown item."},
        409: {
            "model": ErrorRead,
            "description": "Item deactivated, or stock would go negative.",
        },
    },
    summary="Record a stock movement",
    description=(
        "Applies the movement and updates the item quantity atomically. "
        "The caller is taken from the `X-User-Name` and `X-User-Role` headers."
    ),
)
def record_movement(
    item_id: int, payload: MovementCreate, stock: StockDep, actor: ActorDep
):
    return stock.record_movement(
        item_id,
        movement_type=payload.type,
        quantity=payload.quantity,
        performed_by=actor.name,
        role=actor.role,
        note=payload.note,
    )


@router.get(
    "/items/{item_id}/movements",
    response_model=list[MovementRead],
    responses={404: {"model": ErrorRead, "description": "Unknown item."}},
    summary="Movement history for one item",
)
def item_history(item_id: int, stock: StockDep):
    return stock.history(item_id)


@router.get(
    "/movements",
    response_model=list[MovementRead],
    summary="Full movement history",
)
def full_history(stock: StockDep):
    return stock.history()
