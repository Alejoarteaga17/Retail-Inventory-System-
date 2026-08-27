"""Item catalog endpoints."""

from fastapi import APIRouter, Query, status

from api.dependencies import CatalogDep
from api.schemas import ErrorRead, ItemCreate, ItemRead, ItemUpdate

router = APIRouter(prefix="/items", tags=["Item catalog"])


@router.get("", response_model=list[ItemRead], summary="List inventory items")
def list_items(
    catalog: CatalogDep,
    category: str | None = Query(default=None, description="Exact category match."),
    low_stock: bool | None = Query(
        default=None, description="Keep only items at or below their threshold."
    ),
    include_inactive: bool = Query(
        default=False, description="Include deactivated items."
    ),
    q: str | None = Query(default=None, description="Substring match on name or SKU."),
):
    return catalog.list(
        category=category,
        low_stock=low_stock,
        include_inactive=include_inactive,
        search=q,
    )


@router.post(
    "",
    response_model=ItemRead,
    status_code=status.HTTP_201_CREATED,
    responses={409: {"model": ErrorRead, "description": "SKU already in use."}},
    summary="Create an inventory item",
)
def create_item(payload: ItemCreate, catalog: CatalogDep):
    return catalog.create(**payload.model_dump())


@router.get(
    "/{item_id}",
    response_model=ItemRead,
    responses={404: {"model": ErrorRead, "description": "Unknown item."}},
    summary="Get a single inventory item",
)
def get_item(item_id: int, catalog: CatalogDep):
    return catalog.get(item_id)


@router.patch(
    "/{item_id}",
    response_model=ItemRead,
    responses={
        404: {"model": ErrorRead, "description": "Unknown item."},
        409: {"model": ErrorRead, "description": "SKU already in use."},
    },
    summary="Update an inventory item",
)
def update_item(item_id: int, payload: ItemUpdate, catalog: CatalogDep):
    return catalog.update(item_id, payload.model_dump(exclude_unset=True))


@router.delete(
    "/{item_id}",
    response_model=ItemRead,
    responses={404: {"model": ErrorRead, "description": "Unknown item."}},
    summary="Deactivate an inventory item",
    description="Soft delete: the item is retired but its history is preserved.",
)
def deactivate_item(item_id: int, catalog: CatalogDep):
    return catalog.deactivate(item_id)


@router.post(
    "/{item_id}/reactivate",
    response_model=ItemRead,
    responses={404: {"model": ErrorRead, "description": "Unknown item."}},
    summary="Reactivate a deactivated item",
)
def reactivate_item(item_id: int, catalog: CatalogDep):
    return catalog.reactivate(item_id)
