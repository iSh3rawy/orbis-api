import uuid
from datetime import date, datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    username: str
    email: EmailStr
    display_name: str | None = None
    bio: str | None = None
    avatar_url: str | None = None
    banner_url: str | None = None
    location: str | None = None
    website: str | None = None
    date_of_birth: date | None = None
    is_verified: bool
    is_private: bool
    created_at: datetime
