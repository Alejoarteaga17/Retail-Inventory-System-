"""In-memory persistence.

The repository interface is what the services depend on, so swapping this for
a SQL-backed implementation later is a one-file change: the services, the
rules and the routers stay untouched.
"""

from itertools import count
from threading import Lock

from data.inventory_seed import MOCK_ITEMS
from domain.entities import Item, StockMovement


class InMemoryItemRepository:
    """Stores inventory items keyed by id."""

    def __init__(self, seed: list[dict] | None = None) -> None:
        self._items: dict[int, Item] = {}
        self._ids = count(1)
        self._lock = Lock()
        for row in seed if seed is not None else MOCK_ITEMS:
            self.add(Item(id=next(self._ids), **row))

    def add(self, item: Item) -> Item:
        with self._lock:
            self._items[item.id] = item
        return item

    def create(self, **fields) -> Item:
        with self._lock:
            item = Item(id=next(self._ids), **fields)
            self._items[item.id] = item
        return item

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def get_by_sku(self, sku: str) -> Item | None:
        normalized = sku.strip().upper()
        return next(
            (i for i in self._items.values() if i.sku.upper() == normalized), None
        )

    def list(self) -> list[Item]:
        return sorted(self._items.values(), key=lambda i: i.id)


class InMemoryMovementRepository:
    """Append-only store for the stock movement history."""

    def __init__(self) -> None:
        self._movements: list[StockMovement] = []
        self._ids = count(1)
        self._lock = Lock()

    def next_id(self) -> int:
        return next(self._ids)

    def add(self, movement: StockMovement) -> StockMovement:
        with self._lock:
            self._movements.append(movement)
        return movement

    def list(self, item_id: int | None = None) -> list[StockMovement]:
        """Newest first; the history screen always reads in reverse order."""
        movements = self._movements
        if item_id is not None:
            movements = [m for m in movements if m.item_id == item_id]
        return sorted(movements, key=lambda m: m.id, reverse=True)
