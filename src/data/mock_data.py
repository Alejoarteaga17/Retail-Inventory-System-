"""Seed data for Cornerline Home Goods retail inventory catalog."""

MOCK_INVENTORY_ITEMS: list[dict] = [
    {
        "id": 1,
        "name": "Oak Dining Table - 6 Seater",
        "current_quantity": 12,
        "reorder_threshold": 5,
        "is_active": True,
    },
    {
        "id": 2,
        "name": "Linen Sectional Sofa - Gray",
        "current_quantity": 8,
        "reorder_threshold": 3,
        "is_active": True,
    },
    {
        "id": 3,
        "name": "Ceramic Table Lamp - White",
        "current_quantity": 45,
        "reorder_threshold": 15,
        "is_active": True,
    },
    {
        "id": 4,
        "name": "Upholstered Dining Chair - Beige",
        "current_quantity": 3,
        "reorder_threshold": 10,
        "is_active": True,
    },
    {
        "id": 5,
        "name": "King Size Platform Bed Frame",
        "current_quantity": 6,
        "reorder_threshold": 4,
        "is_active": True,
    },
    {
        "id": 6,
        "name": "Glass Coffee Table - Rectangular",
        "current_quantity": 0,
        "reorder_threshold": 5,
        "is_active": True,
    },
    {
        "id": 7,
        "name": "Woven Storage Basket - Large",
        "current_quantity": 28,
        "reorder_threshold": 12,
        "is_active": True,
    },
    {
        "id": 8,
        "name": "Velvet Accent Chair - Navy",
        "current_quantity": 2,
        "reorder_threshold": 6,
        "is_active": False,
    },
]
