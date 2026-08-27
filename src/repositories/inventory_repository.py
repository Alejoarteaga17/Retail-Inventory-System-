"""Data access layer for inventory items (in-memory mock store)."""

from copy import deepcopy

from data.mock_data import MOCK_INVENTORY_ITEMS


class InventoryRepository:
    """In-memory repository backed by mock seed data."""

    def __init__(self, seed_items: list[dict] | None = None) -> None:
        items = seed_items if seed_items is not None else MOCK_INVENTORY_ITEMS
        self._items: dict[int, dict] = {
            item["id"]: deepcopy(item) for item in items
        }
        self._next_id = max(self._items.keys(), default=0) + 1

    def list_items(self, *, include_inactive: bool = False) -> list[dict]:
        if include_inactive:
            return [deepcopy(item) for item in self._items.values()]
        return [
            deepcopy(item)
            for item in self._items.values()
            if item["is_active"]
        ]

    def get_by_id(self, item_id: int) -> dict | None:
        item = self._items.get(item_id)
        return deepcopy(item) if item is not None else None

    def create(self, payload: dict) -> dict:
        item = {
            "id": self._next_id,
            "name": payload["name"],
            "current_quantity": payload["current_quantity"],
            "reorder_threshold": payload["reorder_threshold"],
            "is_active": True,
        }
        self._items[item["id"]] = item
        self._next_id += 1
        return deepcopy(item)

    def update(self, item_id: int, payload: dict) -> dict | None:
        item = self._items.get(item_id)
        if item is None:
            return None

        for field, value in payload.items():
            if value is not None:
                item[field] = value

        return deepcopy(item)

    def deactivate(self, item_id: int) -> dict | None:
        item = self._items.get(item_id)
        if item is None:
            return None

        item["is_active"] = False
        return deepcopy(item)
