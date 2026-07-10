from fastapi import APIRouter, Request, Response, Depends, status
from sqlalchemy.orm import Session
from modules.auth.schemas import RegisterRequest, LoginRequest, LoginResponse
from modules.auth.service import authenticate_user
from modules.users.schemas import UserResponse
from modules.users.service import create_user
from core.database import get_db
from core.security import decode_refresh_token
from core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def register(user_in: RegisterRequest, db: Session = Depends(get_db)):
    user = create_user(db, user_in)
    return UserResponse.model_validate(user)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserResponse)
def login(data: LoginRequest, response: Response, db: Session = Depends(get_db)):
    user, access_token, refresh_token = authenticate_user(data, db)

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=60 * 60 * 24 * settings.REFRESH_TOKEN_EXPIRE_DAYS,
        path=f"api/v{settings.API_VERSION}/auth/refresh",
    )

    return LoginResponse(
        user=UserResponse.model_validate(user), access_token=access_token
    )
