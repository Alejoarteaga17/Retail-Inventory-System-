from schemas.alerts import LowStockAlertItem, LowStockAlertList
from schemas.stock_condition import StockCondition
from services.inventory_service import InventoryService


class AlertService:
    """Aggregates inventory items currently in an alert condition.

    This service does not re-implement the OK / LOW_STOCK / OUT_OF_STOCK
    evaluation rule; it reuses InventoryService, which derives
    stock_condition from each item's current_quantity and
    reorder_threshold. This guarantees alert state can never disagree
    with what item views already show.
    """

    def __init__(self, inventory_service: InventoryService) -> None:
        self._inventory_service = inventory_service

    def list_alerts(self) -> LowStockAlertList:
        # Deactivated items are excluded from alert evaluation by definition.
        active_items = self._inventory_service.list_items(include_inactive=False)

        alert_items = [
            item for item in active_items if item.stock_condition is not StockCondition.OK
        ]
        alert_items.sort(key=lambda item: (item.stock_condition.severity, item.id))

        return LowStockAlertList(
            total=len(alert_items),
            items=[LowStockAlertItem(**item.model_dump()) for item in alert_items],
        )
