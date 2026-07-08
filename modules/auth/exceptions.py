from core.exceptions import UnauthorizedError


class InvalidCredentialsError(UnauthorizedError):
    error_code = "INVALID_CREDENTIALS"
    message = "Invalid email or password"


class InvalidTokenError(UnauthorizedError):
    error_code = "INVALID_TOKEN"
    message = "The provided token is invalid or expired"


class MissingRefreshTokenError(UnauthorizedError):
    error_code = "MISSING_REFRESH_TOKEN"
    message = "Refresh token is missing from the request"
