from data.inventory_repository import InventoryRepository
from exceptions.inventory import (
    InventoryItemAlreadyInactiveError,
    InventoryItemNotFoundError,
    InventoryItemUpdateError,
)
from schemas.inventory import (
    InventoryItemCreate,
    InventoryItemResponse,
    InventoryItemUpdate,
)


class InventoryService:
    """Business logic for inventory item management."""

    def __init__(self, repository: InventoryRepository) -> None:
        self._repository = repository

    @staticmethod
    def _to_response(item: dict) -> InventoryItemResponse:
        return InventoryItemResponse(
            id=item["id"],
            name=item["name"],
            current_quantity=item["current_quantity"],
            reorder_threshold=item["reorder_threshold"],
            is_active=item["is_active"],
            is_low_stock=item["current_quantity"] <= item["reorder_threshold"],
        )

    def list_items(self, *, include_inactive: bool = False) -> list[InventoryItemResponse]:
        items = self._repository.list_items(include_inactive=include_inactive)
        return [self._to_response(item) for item in items]

    def get_item(self, item_id: str) -> InventoryItemResponse:
        item = self._repository.get_by_id(item_id)
        if item is None:
            raise InventoryItemNotFoundError(item_id)
        return self._to_response(item)

    def create_item(self, payload: InventoryItemCreate) -> InventoryItemResponse:
        item = self._repository.create(payload.model_dump())
        return self._to_response(item)

    def update_item(
        self,
        item_id: str,
        payload: InventoryItemUpdate,
    ) -> InventoryItemResponse:
        updates = payload.model_dump(exclude_unset=True)
        if not updates:
            raise InventoryItemUpdateError()

        item = self._repository.update(item_id, updates)
        if item is None:
            raise InventoryItemNotFoundError(item_id)

        return self._to_response(item)

    def deactivate_item(self, item_id: str) -> InventoryItemResponse:
        item = self._repository.get_by_id(item_id)
        if item is None:
            raise InventoryItemNotFoundError(item_id)

        if not item["is_active"]:
            raise InventoryItemAlreadyInactiveError(item_id)

        deactivated = self._repository.deactivate(item_id)
        assert deactivated is not None
        return self._to_response(deactivated)
