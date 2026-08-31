from fastapi import APIRouter, Depends, HTTPException, Query, status

from dependencies import get_inventory_service
from exceptions.authorization import InsufficientRoleError
from exceptions.inventory import (
    InventoryItemAlreadyInactiveError,
    InventoryItemNotFoundError,
    InventoryItemUpdateError,
)
from schemas.alerts import ReorderThresholdUpdate
from schemas.inventory import (
    InventoryItemCreate,
    InventoryItemResponse,
    InventoryItemUpdate,
)
from security.roles import UserRole, require_roles
from services.inventory_service import InventoryService

router = APIRouter(prefix="/inventory/items", tags=["Inventory Items"])


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
    item_id: str,
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
    description="Creates a new catalog item after validating required fields.",
)
def create_inventory_item(
    payload: InventoryItemCreate,
    service: InventoryService = Depends(get_inventory_service),
) -> InventoryItemResponse:
    return service.create_item(payload)


@router.put(
    "/{item_id}",
    response_model=InventoryItemResponse,
    summary="Update inventory item",
    responses={
        404: {"description": "Inventory item not found."},
        422: {"description": "No valid fields provided for update."},
    },
)
def update_inventory_item(
    item_id: str,
    payload: InventoryItemUpdate,
    service: InventoryService = Depends(get_inventory_service),
) -> InventoryItemResponse:
    try:
        return service.update_item(item_id, payload)
    except InventoryItemNotFoundError as exc:
        raise _not_found(exc) from exc
    except InventoryItemUpdateError as exc:
        raise _unprocessable(str(exc)) from exc


@router.patch(
    "/{item_id}/threshold",
    response_model=InventoryItemResponse,
    summary="Configure reorder threshold",
    description=(
        "Sets an item's reorder threshold. Restricted to Store Manager and Owner. "
        "Stock condition is re-evaluated automatically on every read."
    ),
    responses={
        403: {"description": "Caller's role is not authorized to configure thresholds."},
        404: {"description": "Inventory item not found."},
        422: {"description": "Reorder threshold must be a non-negative integer."},
    },
)
def configure_reorder_threshold(
    item_id: str,
    payload: ReorderThresholdUpdate,
    service: InventoryService = Depends(get_inventory_service),
    _role: UserRole = Depends(require_roles(UserRole.STORE_MANAGER, UserRole.OWNER)),
) -> InventoryItemResponse:
    try:
        return service.update_threshold(item_id, payload.reorder_threshold)
    except InventoryItemNotFoundError as exc:
        raise _not_found(exc) from exc


@router.patch(
    "/{item_id}/deactivate",
    response_model=InventoryItemResponse,
    summary="Deactivate inventory item",
    responses={
        404: {"description": "Inventory item not found."},
        409: {"description": "Inventory item is already inactive."},
    },
)
def deactivate_inventory_item(
    item_id: str,
    service: InventoryService = Depends(get_inventory_service),
) -> InventoryItemResponse:
    try:
        return service.deactivate_item(item_id)
    except InventoryItemNotFoundError as exc:
        raise _not_found(exc) from exc
    except InventoryItemAlreadyInactiveError as exc:
        raise _conflict(str(exc)) from exc


def _not_found(exc: InventoryItemNotFoundError) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


def _unprocessable(message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=message,
    )


def _conflict(message: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=message)
