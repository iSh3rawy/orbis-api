from fastapi import Depends
from sqlalchemy.orm import Session
from modules.users.models import User
from modules.auth.schemas import LoginRequest, LoginResponse
from modules.users.schemas import UserResponse
from modules.users.service import get_user_by_email
from modules.users.exceptions import InvalidCredentialsError
from core.security import verify_password, create_access_token, create_refresh_token
from core.database import get_db


def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    user: User = get_user_by_email(db, data.email)
    if not user:
        raise InvalidCredentialsError()
    matched = verify_password(data.password, user.password_hash)
    if not matched:
        raise InvalidCredentialsError()
    access_token = create_access_token(subject=str(user.id))
    refresh_token = create_refresh_token(subject=str(user.id))
    return LoginResponse(
        user=UserResponse.model_validate(user),
        access_token=access_token,
        refresh_token=refresh_token,
    )
