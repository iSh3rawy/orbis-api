from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from modules.auth.schemas import RegisterRequest
from modules.users.schemas import UserResponse
from modules.users.service import create_user

from core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def register_user(user_in: RegisterRequest, db: Session = Depends(get_db)):
    user = create_user(db, user_in)
    return UserResponse.model_validate(user)
