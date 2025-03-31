"""Establish endpoints for interacting with users"""

from fastapi import APIRouter

from app.repositories.user import get_users, get_user_id, create_user, update_user
from app.db.database import DbSession
from app.schemas.user import UserCreate, UserUpdate

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(db: DbSession):
    """Retrives all users."""
    return get_users(db)


@router.get("/users/{user_id}", tags=["users"])
async def read_user_id(db: DbSession, user_id: str):
    """Retrieves user by ID."""
    return get_user_id(db, user_id)


@router.post("/users", tags=["users"])
async def create_new_user(db: DbSession, user_data: UserCreate):
    """Creates a user"""
    try:
        validated_model = UserCreate.model_validate(user_data)
        return create_user(db, validated_model)
    except Exception as e:
        print(f"Exception: {e}")


@router.patch("/users/{user_id}", tags=["users"])
async def update_user_info(db: DbSession, user_id: str, user_data: UserUpdate):
    """Updates a user"""
    try:
        return update_user(db, user_id, user_data)
    except Exception as e:
        print(f"Exception: {e}")
