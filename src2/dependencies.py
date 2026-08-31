from fastapi import Depends

from data.inventory_repository import InventoryRepository
from services.alert_service import AlertService
from services.inventory_service import InventoryService

_repository = InventoryRepository()


def get_inventory_repository() -> InventoryRepository:
    return _repository


def get_inventory_service(
    repository: InventoryRepository = Depends(get_inventory_repository),
) -> InventoryService:
    return InventoryService(repository)


def get_alert_service(
    inventory_service: InventoryService = Depends(get_inventory_service),
) -> AlertService:
    return AlertService(inventory_service)
