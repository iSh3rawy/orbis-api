from fastapi import Depends
from sqlalchemy.orm import Session
from modules.users.models import User
from modules.auth.schemas import LoginRequest
from modules.users.service import get_user_by_email
from modules.auth.exceptions import InvalidCredentialsError
from core.security import verify_password, create_access_token, create_refresh_token
from core.database import get_db


def authenticate_user(
    data: LoginRequest, db: Session = Depends(get_db)
) -> tuple[User, str, str]:
    user: User = get_user_by_email(db, data.email)
    if not user:
        raise InvalidCredentialsError()
    matched = verify_password(data.password, user.password_hash)
    if not matched:
        raise InvalidCredentialsError()
    access_token = create_access_token(subject=str(user.id))
    refresh_token = create_refresh_token(subject=str(user.id))

    return user, access_token, refresh_token
