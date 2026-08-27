"""FastAPI route handlers for inventory item management."""

from fastapi import APIRouter, Depends, Query, status

from schemas.inventory_item import (
    InventoryItemCreate,
    InventoryItemResponse,
    InventoryItemUpdate,
)
from services.inventory_service import InventoryItemNotFoundError, InventoryService

router = APIRouter(prefix="/inventory/items", tags=["Inventory Items"])


def get_inventory_service() -> InventoryService:
    from dependencies import inventory_service

    return inventory_service


@router.get(
    "",
    response_model=list[InventoryItemResponse],
    summary="List inventory items",
    description="Returns the item catalog with current quantity for each item.",
)
def list_inventory_items(
    include_inactive: bool = Query(
        default=False,
        description="Include deactivated items in the response.",
    ),
    service: InventoryService = Depends(get_inventory_service),
) -> list[InventoryItemResponse]:
    return service.list_items(include_inactive=include_inactive)


@router.get(
    "/{item_id}",
    response_model=InventoryItemResponse,
    summary="Get inventory item",
    responses={404: {"description": "Inventory item not found."}},
)
def get_inventory_item(
    item_id: int,
    service: InventoryService = Depends(get_inventory_service),
) -> InventoryItemResponse:
    try:
        return service.get_item(item_id)
    except InventoryItemNotFoundError as exc:
        raise _not_found(exc) from exc


@router.post(
    "",
    response_model=InventoryItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create inventory item",
    description="Validates required fields before adding an item to the catalog.",
)
def create_inventory_item(
    payload: InventoryItemCreate,
    service: InventoryService = Depends(get_inventory_service),
) -> InventoryItemResponse:
    return service.create_item(payload)


@router.patch(
    "/{item_id}",
    response_model=InventoryItemResponse,
    summary="Update inventory item",
    responses={404: {"description": "Inventory item not found."}},
)
def update_inventory_item(
    item_id: int,
    payload: InventoryItemUpdate,
    service: InventoryService = Depends(get_inventory_service),
) -> InventoryItemResponse:
    try:
        return service.update_item(item_id, payload)
    except InventoryItemNotFoundError as exc:
        raise _not_found(exc) from exc


@router.post(
    "/{item_id}/deactivate",
    response_model=InventoryItemResponse,
    summary="Deactivate inventory item",
    responses={404: {"description": "Inventory item not found."}},
)
def deactivate_inventory_item(
    item_id: int,
    service: InventoryService = Depends(get_inventory_service),
) -> InventoryItemResponse:
    try:
        return service.deactivate_item(item_id)
    except InventoryItemNotFoundError as exc:
        raise _not_found(exc) from exc


def _not_found(exc: InventoryItemNotFoundError):
    from fastapi import HTTPException

    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=str(exc),
    )
