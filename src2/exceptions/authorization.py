class InsufficientRoleError(Exception):
    """Raised when the caller's role is not permitted to perform an action.

    This is a temporary domain exception used ahead of the full
    authentication/RBAC module (see issue #6). Once that module exists,
    the role check that raises this should be replaced by real auth
    middleware, but the exception (and its 403 mapping) can stay as-is.
    """

    def __init__(self, required_roles: list[str]) -> None:
        self.required_roles = required_roles
        roles = ", ".join(required_roles)
        super().__init__(f"This action requires one of the following roles: {roles}.")
