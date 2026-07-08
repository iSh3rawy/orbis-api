from core.exceptions import UnauthorizedError


class InvalidCredentialsError(UnauthorizedError):
    error_code = "INVALID_CREDENTIALS"
    message = "Invalid email or password"
