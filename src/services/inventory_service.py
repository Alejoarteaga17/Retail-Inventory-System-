"""Business logic for inventory item catalog management."""

from repositories.inventory_repository import InventoryRepository
from schemas.inventory_item import (
    InventoryItemCreate,
    InventoryItemResponse,
    InventoryItemUpdate,
)


class InventoryItemNotFoundError(Exception):
    """Raised when an inventory item does not exist."""

    def __init__(self, item_id: int) -> None:
        self.item_id = item_id
        super().__init__(f"Inventory item {item_id} not found.")


class InventoryService:
    """Application service for inventory catalog operations."""

    def __init__(self, repository: InventoryRepository) -> None:
        self._repository = repository

    def list_items(
        self,
        *,
        include_inactive: bool = False,
    ) -> list[InventoryItemResponse]:
        items = self._repository.list_items(include_inactive=include_inactive)
        return [InventoryItemResponse.model_validate(item) for item in items]

    def get_item(self, item_id: int) -> InventoryItemResponse:
        item = self._repository.get_by_id(item_id)
        if item is None:
            raise InventoryItemNotFoundError(item_id)
        return InventoryItemResponse.model_validate(item)

    def create_item(self, payload: InventoryItemCreate) -> InventoryItemResponse:
        item = self._repository.create(payload.model_dump())
        return InventoryItemResponse.model_validate(item)

    def update_item(
        self,
        item_id: int,
        payload: InventoryItemUpdate,
    ) -> InventoryItemResponse:
        update_data = payload.model_dump(exclude_unset=True)
        if not update_data:
            return self.get_item(item_id)

        item = self._repository.update(item_id, update_data)
        if item is None:
            raise InventoryItemNotFoundError(item_id)
        return InventoryItemResponse.model_validate(item)

    def deactivate_item(self, item_id: int) -> InventoryItemResponse:
        item = self._repository.deactivate(item_id)
        if item is None:
            raise InventoryItemNotFoundError(item_id)
        return InventoryItemResponse.model_validate(item)
