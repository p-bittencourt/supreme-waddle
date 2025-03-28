"""Pydantic schemas for data validation"""

from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    """Base user model with common attributes"""

    name: str = Field(min_length=1)
    email: EmailStr


class UserCreate(UserBase):
    """Used when creating a new user (no ID yet)"""

    id: int


class UserUpdate(BaseModel):
    """Used when updating an user (all fields optional)"""

    name: str = Field(None, min_length=1)
    email: Optional[EmailStr]


class UserResponse(UserBase):
    """Full user model returned to clients"""

    id: int

    class Config:
        """Configuration for response serialization.

        The from_attributes=True setting allows the model to read data from
        SQLAlchemy ORM models, converting model attributes to schema fields.
        """

        from_attributes = True
