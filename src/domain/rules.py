"""Business rules that govern stock movements.

Kept as free functions over entities so they are trivially testable and hold
regardless of where the data comes from.
"""

from domain.entities import Item
from domain.enums import MovementType, UserRole
from domain.errors import (
    InactiveItem,
    InsufficientStock,
    NotAuthorized,
)


def resulting_quantity(item: Item, movement_type: MovementType, quantity: int) -> int:
    """Quantity the item would hold after applying the movement.

    STOCK_IN adds, STOCK_OUT subtracts, and ADJUSTMENT sets the counted value
    (a physical recount overrides the system, it does not add to it).
    """
    if movement_type is MovementType.STOCK_IN:
        return item.quantity + quantity
    if movement_type is MovementType.STOCK_OUT:
        return item.quantity - quantity
    return quantity


def ensure_movement_allowed(
    item: Item,
    movement_type: MovementType,
    quantity: int,
    role: UserRole,
) -> int:
    """Validate a movement and return the resulting quantity.

    Enforces, in order:
      1. movements are rejected on deactivated items;
      2. manual adjustments require Store Manager or Owner;
      3. stock can never go negative.
    """
    if not item.is_active:
        raise InactiveItem(item.id)

    if movement_type is MovementType.ADJUSTMENT and not role.can_adjust_stock:
        raise NotAuthorized("perform manual stock adjustments", role.value)

    new_quantity = resulting_quantity(item, movement_type, quantity)
    if new_quantity < 0:
        raise InsufficientStock(item.id, item.quantity, quantity)

    return new_quantity
