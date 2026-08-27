"""Domain-level errors.

These carry no HTTP knowledge on purpose: the API layer decides how each one
maps to a status code (see `api/errors.py`).
"""


class DomainError(Exception):
    """Base class for every business-rule violation."""


class ItemNotFound(DomainError):
    def __init__(self, item_id: int) -> None:
        super().__init__(f"Inventory item {item_id} does not exist.")
        self.item_id = item_id


class DuplicateSku(DomainError):
    def __init__(self, sku: str) -> None:
        super().__init__(f"An inventory item with SKU '{sku}' already exists.")
        self.sku = sku


class InactiveItem(DomainError):
    def __init__(self, item_id: int) -> None:
        super().__init__(
            f"Inventory item {item_id} is deactivated and cannot be moved."
        )
        self.item_id = item_id


class InsufficientStock(DomainError):
    def __init__(self, item_id: int, available: int, requested: int) -> None:
        super().__init__(
            f"Inventory item {item_id} has {available} unit(s) available, "
            f"but {requested} were requested."
        )
        self.item_id = item_id
        self.available = available
        self.requested = requested


class NotAuthorized(DomainError):
    def __init__(self, action: str, role: str) -> None:
        super().__init__(f"Role '{role}' is not allowed to {action}.")
        self.action = action
        self.role = role
