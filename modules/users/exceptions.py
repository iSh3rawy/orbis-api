from core.exceptions import ConflictError


class EmailAlreadyExistsError(ConflictError):
    error_code = "EMAIL_ALREADY_EXISTS"
    message = "An account with this email already exists"
