from fastapi import Depends

from data.inventory_repository import InventoryRepository
from services.inventory_service import InventoryService

_repository = InventoryRepository()


def get_inventory_repository() -> InventoryRepository:
    return _repository


def get_inventory_service(
    repository: InventoryRepository = Depends(get_inventory_repository),
) -> InventoryService:
    return InventoryService(repository)
