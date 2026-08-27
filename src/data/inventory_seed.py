"""Mock inventory dataset for Cornerline Home Goods.

Shaped after `docs/proposals/statement-of-work-01.md` (item identifier, name,
current quantity, reorder threshold) and the home-goods catalog implied by
`docs/design.md`. It stands in for the database until the real store is wired
in, and is deliberately seeded with items above, at, and below their reorder
threshold so low-stock alerts can be exercised end to end.
"""

MOCK_ITEMS: list[dict] = [
    {
        "sku": "FUR-CHR-001",
        "name": "Oak Dining Chair",
        "category": "Furniture",
        "quantity": 24,
        "reorder_threshold": 10,
    },
    {
        "sku": "FUR-TBL-002",
        "name": "Walnut Coffee Table",
        "category": "Furniture",
        "quantity": 7,
        "reorder_threshold": 5,
    },
    {
        "sku": "DEC-VAS-010",
        "name": "Ceramic Vase",
        "category": "Decor",
        "quantity": 6,
        "reorder_threshold": 8,
    },
    {
        "sku": "DEC-LMP-011",
        "name": "Brass Table Lamp",
        "category": "Decor",
        "quantity": 12,
        "reorder_threshold": 12,
    },
    {
        "sku": "TEX-SHT-020",
        "name": "Cotton Bed Sheet Set",
        "category": "Textiles",
        "quantity": 42,
        "reorder_threshold": 15,
    },
    {
        "sku": "TEX-TWL-021",
        "name": "Linen Bath Towel",
        "category": "Textiles",
        "quantity": 3,
        "reorder_threshold": 20,
    },
    {
        "sku": "KIT-PAN-030",
        "name": "Cast Iron Skillet",
        "category": "Kitchen",
        "quantity": 18,
        "reorder_threshold": 6,
    },
    {
        "sku": "KIT-MUG-031",
        "name": "Stoneware Mug",
        "category": "Kitchen",
        "quantity": 0,
        "reorder_threshold": 24,
        "is_active": False,
    },
]
