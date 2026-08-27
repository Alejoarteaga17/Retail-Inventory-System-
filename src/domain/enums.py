"""Domain vocabulary shared by every layer."""

from enum import Enum


class MovementType(str, Enum):
    """Kinds of stock movement recorded by the system."""

    STOCK_IN = "STOCK_IN"
    STOCK_OUT = "STOCK_OUT"
    ADJUSTMENT = "ADJUSTMENT"


class UserRole(str, Enum):
    """Roles defined in the SOW. Owner > Store Manager > Store Staff."""

    STORE_STAFF = "STORE_STAFF"
    STORE_MANAGER = "STORE_MANAGER"
    OWNER = "OWNER"

    @property
    def can_adjust_stock(self) -> bool:
        """Manual adjustments are restricted to managers and owners."""
        return self in (UserRole.STORE_MANAGER, UserRole.OWNER)
