"""Request/response contracts.

Separate from `domain.entities` on purpose: the wire format can evolve
(versioned endpoints, extra fields) without dragging the domain along.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator

from domain.enums import MovementType


class ItemCreate(BaseModel):
    sku: str = Field(min_length=3, max_length=32, examples=["FUR-CHR-001"])
    name: str = Field(min_length=1, max_length=120, examples=["Oak Dining Chair"])
    category: str = Field(min_length=1, max_length=60, examples=["Furniture"])
    quantity: int = Field(ge=0, description="Opening quantity on hand.")
    reorder_threshold: int = Field(
        ge=0, description="Quantity at which a low-stock alert is raised."
    )


class ItemUpdate(BaseModel):
    """Partial update. `quantity` is absent by design: it only changes
    through a recorded stock movement."""

    model_config = ConfigDict(extra="forbid")

    sku: str | None = Field(default=None, min_length=3, max_length=32)
    name: str | None = Field(default=None, min_length=1, max_length=120)
    category: str | None = Field(default=None, min_length=1, max_length=60)
    reorder_threshold: int | None = Field(default=None, ge=0)


class ItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    sku: str
    name: str
    category: str
    quantity: int
    reorder_threshold: int
    is_active: bool
    is_low_stock: bool
    created_at: datetime
    updated_at: datetime


class MovementCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: MovementType
    quantity: int = Field(
        ge=0,
        description=(
            "Units moved. For ADJUSTMENT this is the counted quantity on hand, "
            "which replaces the current value rather than adding to it."
        ),
    )
    note: str | None = Field(default=None, max_length=280)

    @model_validator(mode="after")
    def _reject_empty_transfer(self) -> "MovementCreate":
        """A zero-unit stock-in or stock-out is a no-op, not a movement.

        Zero stays legal for ADJUSTMENT: counting an empty shelf is a real
        correction worth recording.
        """
        if self.type is not MovementType.ADJUSTMENT and self.quantity == 0:
            raise ValueError(
                f"{self.type.value} requires a quantity greater than zero."
            )
        return self


class MovementRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    item_id: int
    type: MovementType
    quantity: int
    resulting_quantity: int
    performed_by: str
    performed_by_role: str
    note: str | None
    occurred_at: datetime


class DashboardRead(BaseModel):
    total_items: int
    total_units: int
    low_stock_count: int
    out_of_stock_count: int
    categories: list[str]
    low_stock_items: list[ItemRead]


class ErrorRead(BaseModel):
    """Uniform error envelope for every handled failure."""

    error: str = Field(examples=["ItemNotFound"])
    detail: str = Field(examples=["Inventory item 99 does not exist."])
