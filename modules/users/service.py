from sqlalchemy import select
from sqlalchemy.orm import Session

from modules.auth.schemas import UserCreateRequest
from modules.users.models import User
from modules.users.exceptions import EmailAlreadyExistsError
from core.security import hash_password


def create_user(db: Session, user_in: UserCreateRequest):
    stmt = select(User).where(User.email == user_in.email)
    existing_user = db.execute(stmt).scalar_one_or_none()
    if existing_user:
        raise EmailAlreadyExistsError()
    user = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hash_password(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    stmt = select(User).where(User.username == username)
    result = db.execute(stmt).scalar_one_or_none()
    return result


def get_user_by_email(db: Session, email: str):
    stmt = select(User).where(User.email == email)
    result = db.execute(stmt).scalar_one_or_none()
    return result


def get_user_by_id(db: Session, id: int):
    stmt = select(User).where(User.id == id)
    result = db.execute(stmt).scalar_one_or_none()
    return result
