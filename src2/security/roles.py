"""Temporary authorization stub.

This module exists ONLY to satisfy the authorization requirement of the
Low Stock Alerts feature (issue #3) before real authentication exists
(issue #6, "Add Authentication and Role-Based Access Control").

There is no login, no token, and no identity verification here: the
caller's role is read directly from an `X-User-Role` header. This is
intentionally insecure and MUST be replaced once issue #6 lands. The
role check itself (`require_roles`) is written as a normal FastAPI
dependency so that swapping the identity source later (JWT, session,
etc.) only requires changing `get_current_user_role`, not the routers
that depend on it.
"""

from enum import Enum

from fastapi import Depends, Header, HTTPException, status

from exceptions.authorization import InsufficientRoleError


class UserRole(str, Enum):
    STORE_STAFF = "store_staff"
    STORE_MANAGER = "store_manager"
    OWNER = "owner"


def get_current_user_role(
    x_user_role: str = Header(
        default=UserRole.STORE_STAFF.value,
        description=(
            "TEMPORARY: identifies the caller's role until real authentication "
            "(issue #6) exists. One of: store_staff, store_manager, owner."
        ),
    ),
) -> UserRole:
    """Resolve the caller's role from the X-User-Role header."""
    try:
        return UserRole(x_user_role.lower())
    except ValueError as exc:
        valid_roles = ", ".join(role.value for role in UserRole)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid X-User-Role header. Must be one of: {valid_roles}.",
        ) from exc


def require_roles(*allowed_roles: UserRole):
    """Dependency factory: raises InsufficientRoleError if the caller's role isn't allowed."""

    def verify(role: UserRole = Depends(get_current_user_role)) -> UserRole:
        if role not in allowed_roles:
            raise InsufficientRoleError([r.value for r in allowed_roles])
        return role

    return verify
