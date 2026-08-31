class InventoryItemNotFoundError(Exception):
    """Raised when an inventory item does not exist."""

    def __init__(self, item_id: str) -> None:
        self.item_id = item_id
        super().__init__(f"Inventory item '{item_id}' was not found.")


class InventoryItemAlreadyInactiveError(Exception):
    """Raised when attempting to deactivate an already inactive item."""

    def __init__(self, item_id: str) -> None:
        self.item_id = item_id
        super().__init__(f"Inventory item '{item_id}' is already inactive.")


class InventoryItemUpdateError(Exception):
    """Raised when an update request contains no valid fields."""

    def __init__(self) -> None:
        super().__init__("At least one field must be provided to update an inventory item.")
