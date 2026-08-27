"""Item catalog use cases (create, update, view, deactivate)."""

from data.repositories import InMemoryItemRepository
from domain.entities import Item
from domain.errors import DuplicateSku, ItemNotFound


class CatalogService:
    def __init__(self, items: InMemoryItemRepository) -> None:
        self._items = items

    def get(self, item_id: int) -> Item:
        item = self._items.get(item_id)
        if item is None:
            raise ItemNotFound(item_id)
        return item

    def list(
        self,
        *,
        category: str | None = None,
        low_stock: bool | None = None,
        include_inactive: bool = False,
        search: str | None = None,
    ) -> list[Item]:
        items = self._items.list()
        if not include_inactive:
            items = [i for i in items if i.is_active]
        if category:
            items = [i for i in items if i.category.lower() == category.lower()]
        if low_stock is not None:
            items = [i for i in items if i.is_low_stock is low_stock]
        if search:
            needle = search.strip().lower()
            items = [
                i
                for i in items
                if needle in i.name.lower() or needle in i.sku.lower()
            ]
        return items

    def create(
        self,
        *,
        sku: str,
        name: str,
        category: str,
        quantity: int,
        reorder_threshold: int,
    ) -> Item:
        normalized_sku = sku.strip().upper()
        if self._items.get_by_sku(normalized_sku) is not None:
            raise DuplicateSku(normalized_sku)
        return self._items.create(
            sku=normalized_sku,
            name=name.strip(),
            category=category.strip(),
            quantity=quantity,
            reorder_threshold=reorder_threshold,
        )

    def update(self, item_id: int, changes: dict) -> Item:
        """Patch catalog attributes.

        `quantity` is intentionally not patchable: quantities only change
        through a recorded stock movement, so the audit trail stays complete.
        """
        item = self.get(item_id)
        if "sku" in changes:
            new_sku = changes["sku"].strip().upper()
            existing = self._items.get_by_sku(new_sku)
            if existing is not None and existing.id != item.id:
                raise DuplicateSku(new_sku)
            changes = {**changes, "sku": new_sku}

        for field_name, value in changes.items():
            setattr(item, field_name, value)
        item.touch()
        return item

    def deactivate(self, item_id: int) -> Item:
        """Soft delete. Inventory records are never destroyed, only retired."""
        item = self.get(item_id)
        item.is_active = False
        item.touch()
        return item

    def reactivate(self, item_id: int) -> Item:
        item = self.get(item_id)
        item.is_active = True
        item.touch()
        return item
