from enum import Enum


class StockCondition(str, Enum):
    """Stock condition of an inventory item, derived from quantity vs. threshold.

    OUT_OF_STOCK takes precedence over LOW_STOCK: an item with quantity zero
    is always OUT_OF_STOCK regardless of its reorder threshold.
    """

    OK = "OK"
    LOW_STOCK = "LOW_STOCK"
    OUT_OF_STOCK = "OUT_OF_STOCK"

    @classmethod
    def evaluate(cls, *, current_quantity: int, reorder_threshold: int) -> "StockCondition":
        """Classify an item's stock condition from its quantity and threshold."""
        if current_quantity == 0:
            return cls.OUT_OF_STOCK
        if current_quantity <= reorder_threshold:
            return cls.LOW_STOCK
        return cls.OK

    @property
    def severity(self) -> int:
        """Lower value sorts first (more urgent) in alert listings."""
        order = {
            StockCondition.OUT_OF_STOCK: 0,
            StockCondition.LOW_STOCK: 1,
            StockCondition.OK: 2,
        }
        return order[self]
