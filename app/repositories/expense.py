"""Handles interacting with the users table on the database"""

from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import engine
from app.models.user import User

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.models.user import User
from app.models.expense import Expense


def retrieve_expenses() -> List[Expense]:
    """Retrieves all users from the db"""
    with Session(engine) as session:
        try:
            expenses = session.scalars(select(Expense)).all()
            return expenses
        except Exception as e:
            print("Something went wrong: ", str(e))
            raise


def retrieve_expense_id(expenseId: str) -> Expense:
    """Retrieves expense by id"""
    with Session(engine) as session:
        try:
            expense = session.scalar(select(Expense).where(Expense.id == expenseId))
            return expense
        except Exception as e:
            print("Something went wrong: ", str(e))
            raise


retrieve_expenses()
retrieve_expense_id(10)
