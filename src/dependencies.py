"""Application-wide dependency wiring."""

from repositories.inventory_repository import InventoryRepository
from services.inventory_service import InventoryService

inventory_repository = InventoryRepository()
inventory_service = InventoryService(inventory_repository)
