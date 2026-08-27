"""Low-stock alerts, dashboard metrics and reporting."""

from data.repositories import InMemoryItemRepository
from domain.entities import Item


class InsightsService:
    def __init__(self, items: InMemoryItemRepository) -> None:
        self._items = items

    def low_stock_items(self) -> list[Item]:
        """Active items whose quantity reached or fell below their threshold.

        Ordered by how deep into the threshold they are, so whatever is most
        urgent to reorder shows up first.
        """
        low = [i for i in self._items.list() if i.is_low_stock]
        return sorted(low, key=lambda i: i.quantity - i.reorder_threshold)

    def dashboard(self) -> dict:
        active = [i for i in self._items.list() if i.is_active]
        low = self.low_stock_items()
        return {
            "total_items": len(active),
            "total_units": sum(i.quantity for i in active),
            "low_stock_count": len(low),
            "out_of_stock_count": sum(1 for i in active if i.quantity == 0),
            "categories": sorted({i.category for i in active}),
            "low_stock_items": low,
        }
