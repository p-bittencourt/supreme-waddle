"""Establish endpoints for interacting with users"""

from fastapi import APIRouter

from app.repositories.user import (
    get_users,
    get_user_id,
    create_user,
    update_user,
    delete_user,
)
from app.db.database import DbSession
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponse])
async def read_users(db: DbSession):
    """Retrives all users."""
    return get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
async def read_user_id(db: DbSession, user_id: str):
    """Retrieves user by ID."""
    return get_user_id(db, user_id)


@router.post("/", response_model=UserResponse)
async def create_new_user(db: DbSession, user_data: UserCreate):
    """Creates a user"""
    return create_user(db, user_data)


@router.patch("/{user_id}", response_model=UserResponse)
async def update_user_info(db: DbSession, user_id: str, user_data: UserUpdate):
    """Updates a user"""
    return update_user(db, user_id, user_data)


@router.delete("/{user_id}")
async def delete_user_data(db: DbSession, user_id: str):
    """Deletes a user"""
    return delete_user(db, user_id)
