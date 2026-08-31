from fastapi import APIRouter, Depends

from dependencies import get_alert_service
from schemas.alerts import LowStockAlertList
from services.alert_service import AlertService

router = APIRouter(prefix="/inventory/alerts", tags=["Inventory Alerts"])


@router.get(
    "",
    response_model=LowStockAlertList,
    summary="List low-stock alerts",
    description=(
        "Returns all active inventory items currently in a LOW_STOCK or "
        "OUT_OF_STOCK condition, ordered by severity (out-of-stock first). "
        "Deactivated items are always excluded. Available to any authenticated role."
    ),
)
def list_low_stock_alerts(
    service: AlertService = Depends(get_alert_service),
) -> LowStockAlertList:
    return service.list_alerts()
