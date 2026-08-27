from pydantic import BaseModel, ConfigDict, Field


class InventoryItemBase(BaseModel):
    """Shared fields for inventory catalog items."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Display name of the inventory item.",
    )
    current_quantity: int = Field(
        ...,
        ge=0,
        description="Units currently available in stock.",
    )
    reorder_threshold: int = Field(
        ...,
        ge=0,
        description="Minimum quantity before a low-stock alert is triggered.",
    )


class InventoryItemCreate(InventoryItemBase):
    """Payload for creating a new inventory item."""


class InventoryItemUpdate(BaseModel):
    """Payload for updating an existing inventory item."""

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Display name of the inventory item.",
    )
    current_quantity: int | None = Field(
        default=None,
        ge=0,
        description="Units currently available in stock.",
    )
    reorder_threshold: int | None = Field(
        default=None,
        ge=0,
        description="Minimum quantity before a low-stock alert is triggered.",
    )


class InventoryItemResponse(InventoryItemBase):
    """Inventory item returned by the API."""

    id: int = Field(..., description="Unique identifier for the inventory item.")
    is_active: bool = Field(
        ...,
        description="Whether the item is active in the catalog.",
    )

    model_config = ConfigDict(from_attributes=True)
