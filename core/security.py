import jwt
from datetime import datetime, timedelta, timezone
from typing import Any
from pwdlib import PasswordHash

from core.config import settings

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(subject: str) -> str:
    expire = datetime.now(tz=timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
        "type": "access_token",
    }
    encoded_jwt = jwt.encode(
        payload, settings.ACCESS_TOKEN_SECRET, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(subject: str) -> str:
    expire = datetime.now(tz=timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )
    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
        "type": "refresh_token",
    }
    encoded_jwt = jwt.encode(
        payload, settings.REFRESH_TOKEN_SECRET, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


def decode_access_token(token: str) -> dict[str, Any]:
    return jwt.decode(
        token, settings.ACCESS_TOKEN_SECRET, algorithms=[settings.JWT_ALGORITHM]
    )


def decode_refresh_token(token: str) -> dict[str, Any]:
    return jwt.decode(
        token, settings.REFRESH_TOKEN_SECRET, algorithms=[settings.JWT_ALGORITHM]
    )
