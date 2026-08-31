from copy import deepcopy

from data.mock_data import INITIAL_INVENTORY_ITEMS


class InventoryRepository:
    """In-memory persistence layer for inventory items."""

    def __init__(self, seed_items: list[dict] | None = None) -> None:
        items = seed_items if seed_items is not None else INITIAL_INVENTORY_ITEMS
        self._items: dict[str, dict] = {
            item["id"]: deepcopy(item) for item in items
        }
        self._next_sequence = self._compute_next_sequence()

    def _compute_next_sequence(self) -> int:
        numeric_ids = []
        for item_id in self._items:
            if item_id.startswith("ITM-"):
                suffix = item_id.removeprefix("ITM-")
                if suffix.isdigit():
                    numeric_ids.append(int(suffix))
        return max(numeric_ids, default=0) + 1

    def _generate_id(self) -> str:
        item_id = f"ITM-{self._next_sequence:03d}"
        self._next_sequence += 1
        return item_id

    def list_items(self, *, include_inactive: bool = False) -> list[dict]:
        items = self._items.values()
        if not include_inactive:
            items = [item for item in items if item["is_active"]]
        return sorted(items, key=lambda item: item["id"])

    def get_by_id(self, item_id: str) -> dict | None:
        item = self._items.get(item_id)
        return deepcopy(item) if item else None

    def create(self, payload: dict) -> dict:
        item_id = self._generate_id()
        item = {
            "id": item_id,
            "name": payload["name"],
            "current_quantity": payload["current_quantity"],
            "reorder_threshold": payload["reorder_threshold"],
            "is_active": True,
        }
        self._items[item_id] = item
        return deepcopy(item)

    def update(self, item_id: str, payload: dict) -> dict | None:
        item = self._items.get(item_id)
        if item is None:
            return None

        for field, value in payload.items():
            if value is not None:
                item[field] = value

        return deepcopy(item)

    def deactivate(self, item_id: str) -> dict | None:
        item = self._items.get(item_id)
        if item is None:
            return None

        item["is_active"] = False
        return deepcopy(item)
