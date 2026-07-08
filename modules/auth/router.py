from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from modules.auth.schemas import RegisterRequest, LoginRequest, LoginResponse
from modules.auth.service import login_user
from modules.users.schemas import UserResponse
from modules.users.service import create_user
from core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def register(user_in: RegisterRequest, db: Session = Depends(get_db)):
    user = create_user(db, user_in)
    return UserResponse.model_validate(user)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(data, db)
