from http import HTTPStatus


class HttpExceptionBase(Exception):
    def __init__(
        self,
        message: str = "An error has occurred",
        status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class NotFoundException(HttpExceptionBase):
    def __init__(
        self,
        message: str = "Resource not found",
        status_code: int = HTTPStatus.NOT_FOUND,
    ):
        super().__init__(message, status_code)


class BadRequestException(HttpExceptionBase):
    def __init__(
        self,
        message: str = "Bad request",
        status_code: int = HTTPStatus.BAD_REQUEST,
    ):
        super().__init__(message, status_code)


class IntegrityException(HttpExceptionBase):
    def __init__(
        self,
        message: str = "Data already exists",
        status_code: int = HTTPStatus.BAD_REQUEST,
    ):
        super().__init__(message, status_code)
