"""Handles interacting with the users table on the database"""

from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.models.user import User
from app.models.expense import Expense  # pylint: disable=unused-import
from app.schemas.user import UserCreate, UserUpdate


def get_users(db: Session) -> List[User]:
    """Retrieves all users from the db"""
    users = db.scalars(select(User)).all()
    return users


def get_user_id(db: Session, user_id: str) -> User:
    """Retrieves user by id"""
    user = db.scalar(select(User).where(User.id == user_id))
    return user


def create_user(db: Session, user_data: UserCreate) -> User:
    """Adds a user to the db"""
    new_user = User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: str, user_data: UserUpdate) -> User:
    """Updates user info"""
    # Get only fields that are provided
    update_data = {k: v for k, v in user_data.model_dump().items() if v is not None}

    # If no update data provided
    if not update_data:
        # TODO: implement custom error
        pass

    # Query to update on db
    db.query(User).filter(User.id == user_id).update(update_data)
    db.commit()

    # Retrieve updated user
    updated_user = get_user_id(db, user_id)
    return updated_user


def delete_user(db: Session, user_id: str) -> None:
    """Deletes user data"""
    user = get_user_id(db, user_id)
    db.delete(user)
    db.commit()
