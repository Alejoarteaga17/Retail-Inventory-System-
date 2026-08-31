from pydantic import BaseModel, Field

from schemas.inventory import InventoryItemResponse


class ReorderThresholdUpdate(BaseModel):
    """Payload for configuring an item's reorder threshold."""

    reorder_threshold: int = Field(
        ...,
        ge=0,
        description="New reorder threshold. Must be a non-negative integer.",
    )


class LowStockAlertItem(InventoryItemResponse):
    """An inventory item currently in an alert condition (LOW_STOCK or OUT_OF_STOCK)."""


class LowStockAlertList(BaseModel):
    """Response payload for the low-stock alert list."""

    total: int = Field(..., description="Number of items currently in an alert condition.")
    items: list[LowStockAlertItem] = Field(
        default_factory=list,
        description="Items in an alert condition, ordered by severity (OUT_OF_STOCK first).",
    )
