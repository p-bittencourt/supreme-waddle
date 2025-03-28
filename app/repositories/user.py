"""Handles interacting with the users table on the database"""

from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import engine

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.models.user import User
from app.models.expense import Expense  # pylint: disable=unused-import


def retrieve_users() -> List[User]:
    """Retrieves all users from the db"""
    with Session(engine) as session:
        try:
            users = session.scalars(select(User)).all()
            return users
        except Exception as e:
            print("Something went wrong: ", str(e))
            raise


def retrieve_user_id(user_id: str) -> User:
    """Retrieves user by id"""
    with Session(engine) as session:
        try:
            user = session.scalar(select(User).where(User.id == user_id))
            return user
        except Exception as e:
            print("Something went wrong: ", str(e))
            raise


retrieve_users()
retrieve_user_id(6)
