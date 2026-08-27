"""Translation of domain errors into HTTP responses.

Routers stay free of status codes: they call a service and let a raised
`DomainError` become the right response here.
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from domain.errors import (
    DomainError,
    DuplicateSku,
    InactiveItem,
    InsufficientStock,
    ItemNotFound,
    NotAuthorized,
)

_STATUS_BY_ERROR: dict[type[DomainError], int] = {
    ItemNotFound: status.HTTP_404_NOT_FOUND,
    NotAuthorized: status.HTTP_403_FORBIDDEN,
    DuplicateSku: status.HTTP_409_CONFLICT,
    InactiveItem: status.HTTP_409_CONFLICT,
    InsufficientStock: status.HTTP_409_CONFLICT,
}


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DomainError)
    async def handle_domain_error(_: Request, exc: DomainError) -> JSONResponse:
        status_code = _STATUS_BY_ERROR.get(
            type(exc), status.HTTP_422_UNPROCESSABLE_ENTITY
        )
        return JSONResponse(
            status_code=status_code,
            content={"error": type(exc).__name__, "detail": str(exc)},
        )
