from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr


class UserCreate(UserBase):
    id: int


class UserUpdate(BaseModel):
    name: str = Field(None, min_length=1)
    email: Optional[EmailStr]


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
