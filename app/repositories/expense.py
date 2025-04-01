"""Handles interacting with the users table on the database"""

import logging
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

# Add imports to ensure both models are fully loaded before SQLAlchemy tries to map the relationships
from app.exceptions import BadRequest, NotFound
from app.models.user import User  # pylint: disable=unused-import
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate

logger = logging.getLogger(__name__)


def get_filtered_expenses(
    db: Session, user_id: str = None, category: str = None
) -> List[Expense]:
    """Retrives expenses with optional filtering by user_id and category"""
    try:
        query = db.query(Expense)

        if user_id:
            query = query.where(Expense.user_id == user_id)

        if category:
            query = query.where(Expense.category == category)

        expenses = query.all()
        logger.info(
            "Retrieved %d expenses with filters: user_id=%s, category=%s",
            len(expenses),
            user_id,
            category,
        )
        return expenses
    except Exception as e:
        logger.error("Something went wrong: %s", str(e))
        raise BadRequest("Expense")


def get_expense_id(db: Session, expense_id: str) -> Expense:
    """Retrieves expense by id"""
    expense = db.scalar(select(Expense).where(Expense.id == expense_id))
    if not expense:
        logger.warning("Expense %s not found.", expense_id)
        raise NotFound("Expense", expense_id)
    logger.info("Retrieved Expense %s, $%.2f", expense.title, expense.value)
    return expense


def add_expense(db: Session, expense_data: ExpenseCreate) -> Expense:
    """Adds an expense"""
    try:
        new_expense = Expense(**expense_data.model_dump())
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        logger.info("Created Expense %s, $%.2f", new_expense.title, new_expense.value)
        return new_expense
    except Exception as e:
        logger.error("Failed to create expense. Error %s", str(e))
        raise BadRequest("Expense") from e


def update_expense(
    db: Session, expense_id: str, expense_data: ExpenseUpdate
) -> Expense:
    """Updates expense data"""
    # Check if expense exists
    expense = get_expense_id(db, expense_id)

    # Get only fields that are provided
    update_data = {k: v for k, v in expense_data.model_dump().items() if v is not None}

    # If no update data provided
    if not update_data:
        logger.warning("Couldn't update expense #%s", expense_id)
        raise BadRequest("Expense", expense_id)

    # Query to update on db
    db.query(Expense).filter(Expense.id == expense_id).update(update_data)
    db.commit()

    # Refresh the expense object
    db.refresh(expense)
    logger.info("Updated Expense%s, $%.2f", expense.title, expense.value)
    return expense


def delete_expense(db: Session, expense_id: str) -> None:
    """Deletes expense data"""
    expense = get_expense_id(db, expense_id)
    db.delete(expense)
    db.commit()
    logger.info("Expense %s deleted.", expense.title)
