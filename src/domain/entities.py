"""Pure domain entities.

Plain dataclasses with no framework imports, so the business rules can be
reasoned about (and later persisted differently) without touching FastAPI.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone

from domain.enums import MovementType


def _now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class Item:
    """An inventory item in the catalog."""

    id: int
    sku: str
    name: str
    category: str
    quantity: int
    reorder_threshold: int
    is_active: bool = True
    created_at: datetime = field(default_factory=_now)
    updated_at: datetime = field(default_factory=_now)

    @property
    def is_low_stock(self) -> bool:
        """Low stock is reached, not merely crossed (SOW: 'reaches or falls below')."""
        return self.is_active and self.quantity <= self.reorder_threshold

    def touch(self) -> None:
        self.updated_at = _now()


@dataclass
class StockMovement:
    """An immutable audit record of a change in an item's quantity."""

    id: int
    item_id: int
    type: MovementType
    quantity: int
    resulting_quantity: int
    performed_by: str
    performed_by_role: str
    note: str | None = None
    occurred_at: datetime = field(default_factory=_now)
