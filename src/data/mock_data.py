"""Seed data for Cornerline Home Goods inventory catalog."""

INITIAL_INVENTORY_ITEMS: list[dict] = [
    {
        "id": "ITM-001",
        "name": "Ceramic Vase - Ivory",
        "current_quantity": 45,
        "reorder_threshold": 10,
        "is_active": True,
    },
    {
        "id": "ITM-002",
        "name": "Bamboo Cutting Board - Large",
        "current_quantity": 28,
        "reorder_threshold": 8,
        "is_active": True,
    },
    {
        "id": "ITM-003",
        "name": "Cotton Throw Blanket - Sage",
        "current_quantity": 12,
        "reorder_threshold": 15,
        "is_active": True,
    },
    {
        "id": "ITM-004",
        "name": "Scented Candle Set - Lavender",
        "current_quantity": 67,
        "reorder_threshold": 20,
        "is_active": True,
    },
    {
        "id": "ITM-005",
        "name": "Woven Storage Basket - Medium",
        "current_quantity": 5,
        "reorder_threshold": 12,
        "is_active": True,
    },
    {
        "id": "ITM-006",
        "name": "Kitchen Towel Set - Striped",
        "current_quantity": 0,
        "reorder_threshold": 25,
        "is_active": False,
    },
]
