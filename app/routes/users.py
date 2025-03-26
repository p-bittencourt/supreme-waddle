"""Establish endpoints for interacting with users"""

from fastapi import APIRouter

from app.repositories.user import *

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return retrieve_users()


@router.get("/users/{user_id}", tags=["users"])
async def read_user_id(user_id):
    return retrieve_user_id(user_id)


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakeCurrentUser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
