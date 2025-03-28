"""Handles interacting with the users table on the database"""

from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.models.user import User  # pylint: disable=unused-import
from app.models.expense import Expense


def retrieve_expenses(db: Session) -> List[Expense]:
    """Retrieves all users from the db"""
    expenses = db.scalars(select(Expense)).all()
    return expenses


def retrieve_expense_id(db: Session, expense_id: str) -> Expense:
    """Retrieves expense by id"""
    expense = db.scalar(select(Expense).where(Expense.id == expense_id))
    return expense
