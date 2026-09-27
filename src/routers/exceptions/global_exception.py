from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.exceptions import HttpExceptionBase

MESSAGE_ERROR = "Erro interno do servidor. Tente novamente mais tarde."


async def global_exception(
    request: Request,
    exc: Exception,
):
    origem = f"{request.method} {request.url.path}"
    print(origem)

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = MESSAGE_ERROR
    if isinstance(exc, RequestValidationError):
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        message = "Validation error"

    if isinstance(exc, HTTPException):
        status_code = exc.status_code
        message = exc.detail

    if isinstance(exc, HttpExceptionBase):
        status_code = exc.status_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content=message,
    )
