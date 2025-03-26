"""Handles interacting with the users table on the database"""

from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import engine
from app.models.user import User

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.models.user import User
from app.models.expense import Expense


def retrieve_users() -> List[User]:
    """Retrieve all users from the db"""
    with Session(engine) as session:
        try:
            users = session.scalars(select(User)).all()
            return users
        except Exception as e:
            print("Something went wrong: ", str(e))
            raise


def retrieve_user_id(userId: str) -> User:
    """Retrieves user by id"""
    with Session(engine) as session:
        try:
            user = session.scalar(select(User).where(User.id == userId))
            print(user)
        except Exception as e:
            print("Something went wrong: ", str(e))
            raise
