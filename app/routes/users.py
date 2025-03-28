"""Establish endpoints for interacting with users"""

from fastapi import APIRouter

from app.repositories.user import *
from app.db.database import DbSession

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(db: DbSession):
    """Retrives all users."""
    return retrieve_users(db)


@router.get("/users/{user_id}", tags=["users"])
async def read_user_id(db: DbSession, user_id):
    """Retrieves user by ID."""
    return retrieve_user_id(db, user_id)
