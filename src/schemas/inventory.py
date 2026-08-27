from pydantic import BaseModel, ConfigDict, Field


class InventoryItemBase(BaseModel):
    """Shared fields for inventory item requests."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Display name of the inventory item.",
    )
    current_quantity: int = Field(
        ...,
        ge=0,
        description="Current stock quantity available.",
    )
    reorder_threshold: int = Field(
        ...,
        ge=0,
        description="Minimum quantity before a low-stock alert is triggered.",
    )


class InventoryItemCreate(InventoryItemBase):
    """Payload for creating a new inventory item."""


class InventoryItemUpdate(BaseModel):
    """Payload for updating an existing inventory item. At least one field is required."""

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Updated display name.",
    )
    current_quantity: int | None = Field(
        default=None,
        ge=0,
        description="Updated stock quantity.",
    )
    reorder_threshold: int | None = Field(
        default=None,
        ge=0,
        description="Updated reorder threshold.",
    )


class InventoryItemResponse(InventoryItemBase):
    """Inventory item returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: str = Field(..., description="Unique item identifier.")
    is_active: bool = Field(..., description="Whether the item is active in the catalog.")
    is_low_stock: bool = Field(
        ...,
        description="True when current quantity is at or below the reorder threshold.",
    )
