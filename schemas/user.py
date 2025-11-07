from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class UserRead(UserBase):
    id: int
    created_at: int
    updated_at: int

    model_config = {"from_attributes": True}
