class AppException(Exception):
    """Base class for all custom application exceptions."""

    status_code: int = 500
    error_code: str = "internal_error"
    message: str = "An unexpected error occurred"

    def __init__(self, message: str | None = None, **extra):
        self.message = message or self.message
        self.extra = extra
        super().__init__(self.message)


class NotFoundError(AppException):
    status_code = 404
    error_code = "not_found"
    message = "Resource not found"


class UnauthorizedError(AppException):
    status_code = 401
    error_code = "unauthorized"
    message = "Authentication required"


class ForbiddenError(AppException):
    status_code = 403
    error_code = "forbidden"
    message = "You don't have permission to perform this action"


class ConflictError(AppException):
    status_code = 409
    error_code = "conflict"
    message = "Resource already exists"


class ValidationError(AppException):
    status_code = 422
    error_code = "validation_error"
    message = "Invalid input"


class RateLimitError(AppException):
    status_code = 429
    error_code = "rate_limited"
    message = "Too many requests, please try again later"
