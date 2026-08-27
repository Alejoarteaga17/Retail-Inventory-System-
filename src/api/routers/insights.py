"""Low-stock alerts, dashboard and reporting endpoints."""

from fastapi import APIRouter

from api.dependencies import InsightsDep
from api.schemas import DashboardRead, ItemRead

router = APIRouter(prefix="/insights", tags=["Insights"])


@router.get(
    "/low-stock",
    response_model=list[ItemRead],
    summary="Items at or below their reorder threshold",
    description="Most urgent first, ranked by how far below the threshold they sit.",
)
def low_stock(insights: InsightsDep):
    return insights.low_stock_items()


@router.get(
    "/dashboard",
    response_model=DashboardRead,
    summary="Inventory dashboard summary",
)
def dashboard(insights: InsightsDep):
    return insights.dashboard()
