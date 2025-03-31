"""Handles interacting with the users table on the database"""

from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.models.user import User  # pylint: disable=unused-import
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate


def get_expenses(db: Session) -> List[Expense]:
    """Retrieves all users from the db"""
    expenses = db.scalars(select(Expense)).all()
    return expenses


def get_expense_id(db: Session, expense_id: str) -> Expense:
    """Retrieves expense by id"""
    expense = db.scalar(select(Expense).where(Expense.id == expense_id))
    return expense


def add_expense(db: Session, expense_data: ExpenseCreate) -> Expense:
    """Adds an expense"""
    new_expense = Expense(**expense_data.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


def update_expense(
    db: Session, expense_id: str, expense_data: ExpenseUpdate
) -> Expense:
    """Updates expense data"""
    # Get only fields that are provided
    update_data = {k: v for k, v in expense_data.model_dump().items() if v is not None}

    # If no update data provided
    if not update_data:
        # TODO: implement custom error
        pass

    # Query to update on db
    db.query(Expense).filter(Expense.id == expense_id).update(update_data)
    db.commit()

    # Retrieve updated expense
    updated_expense = get_expense_id(db, expense_id)
    return updated_expense


def delete_expense(db: Session, expense_id: str) -> None:
    """Deletes expense data"""
    expense = get_expense_id(db, expense_id)
    db.delete(expense)
    db.commit()
