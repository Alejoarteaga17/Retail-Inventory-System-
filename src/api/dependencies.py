"""Composition root and request-scoped dependencies.

Wiring lives here so routers never build their own services and can be tested
against fakes with `app.dependency_overrides`.
"""

from typing import Annotated

from fastapi import Depends, Header

from data.repositories import InMemoryItemRepository, InMemoryMovementRepository
from domain.enums import UserRole
from services.catalog_service import CatalogService
from services.insights_service import InsightsService
from services.stock_service import StockService

# Single in-memory instance for the process lifetime. Swapping these two lines
# for a real database session is the whole persistence migration.
_item_repository = InMemoryItemRepository()
_movement_repository = InMemoryMovementRepository()

_catalog_service = CatalogService(_item_repository)
_stock_service = StockService(_item_repository, _movement_repository, _catalog_service)
_insights_service = InsightsService(_item_repository)


def get_catalog_service() -> CatalogService:
    return _catalog_service


def get_stock_service() -> StockService:
    return _stock_service


def get_insights_service() -> InsightsService:
    return _insights_service


class Actor:
    """Who is performing the request.

    Authentication is out of scope for this iteration, so the caller is read
    from headers and trusted. The seam is deliberate: when real auth lands,
    only `get_current_actor` changes -- the services already receive a name
    and a role and enforce permissions on them.
    """

    def __init__(self, name: str, role: UserRole) -> None:
        self.name = name
        self.role = role


def get_current_actor(
    x_user_name: Annotated[str, Header()] = "demo.user",
    x_user_role: Annotated[UserRole, Header()] = UserRole.STORE_STAFF,
) -> Actor:
    return Actor(name=x_user_name, role=x_user_role)


CatalogDep = Annotated[CatalogService, Depends(get_catalog_service)]
StockDep = Annotated[StockService, Depends(get_stock_service)]
InsightsDep = Annotated[InsightsService, Depends(get_insights_service)]
ActorDep = Annotated[Actor, Depends(get_current_actor)]
