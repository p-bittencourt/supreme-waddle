"""Establish endpoints for interacting with users"""

from fastapi import APIRouter

from app.repositories.user import *

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    """Retrives all users."""
    return retrieve_users()


@router.get("/users/{user_id}", tags=["users"])
async def read_user_id(user_id):
    """Retrieves user by ID."""
    return retrieve_user_id(user_id)
