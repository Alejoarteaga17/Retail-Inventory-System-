"""Stock movement use cases.

Every quantity change in the system goes through `record_movement`, which is
what keeps the movement history a complete audit trail.
"""

from data.repositories import InMemoryItemRepository, InMemoryMovementRepository
from domain.entities import StockMovement
from domain.enums import MovementType, UserRole
from domain.rules import ensure_movement_allowed
from services.catalog_service import CatalogService


class StockService:
    def __init__(
        self,
        items: InMemoryItemRepository,
        movements: InMemoryMovementRepository,
        catalog: CatalogService,
    ) -> None:
        self._items = items
        self._movements = movements
        self._catalog = catalog

    def record_movement(
        self,
        item_id: int,
        *,
        movement_type: MovementType,
        quantity: int,
        performed_by: str,
        role: UserRole,
        note: str | None = None,
    ) -> StockMovement:
        """Validate, apply and log a stock movement.

        Raises `ItemNotFound` for unknown items, and the rule violations
        defined in `domain.rules`. The item quantity is only written once the
        movement has been fully validated.
        """
        item = self._catalog.get(item_id)
        new_quantity = ensure_movement_allowed(item, movement_type, quantity, role)

        item.quantity = new_quantity
        item.touch()

        return self._movements.add(
            StockMovement(
                id=self._movements.next_id(),
                item_id=item.id,
                type=movement_type,
                quantity=quantity,
                resulting_quantity=new_quantity,
                performed_by=performed_by,
                performed_by_role=role.value,
                note=note,
            )
        )

    def history(self, item_id: int | None = None) -> list[StockMovement]:
        if item_id is not None:
            self._catalog.get(item_id)  # 404 on unknown items
        return self._movements.list(item_id)
