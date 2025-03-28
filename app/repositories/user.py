"""Handles interacting with the users table on the database"""

from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.models.user import User
from app.models.expense import Expense  # pylint: disable=unused-import


def retrieve_users(db: Session) -> List[User]:
    """Retrieves all users from the db"""
    users = db.scalars(select(User)).all()
    return users


def retrieve_user_id(db: Session, user_id: str) -> User:
    """Retrieves user by id"""
    user = db.scalar(select(User).where(User.id == user_id))
    return user
