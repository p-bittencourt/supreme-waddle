"""Test script for Expense crud operations"""

import pytest
from sqlalchemy.orm import Session

from app.models.expense import Expense, ExpenseCategory
from app.schemas.expense import ExpenseCreate
from app.repositories.expense import add_expense, get_expense_id
from tests.factories.user import UserFactory


def test_add_expense(db: Session) -> None:
    """Tests adding an expense to the db"""
    # First create a user
    user = UserFactory()

    title = "Apples and organges"
    value = "5.75"
    category = ExpenseCategory.GROCERIES

    expense_in = ExpenseCreate(
        title=title, value=value, category=category, user_id=user.id
    )

    expense = add_expense(db=db, expense_data=expense_in)

    assert expense.title == title
    assert expense.user_id == user.id
    assert expense.value == float(value)


def test_get_expense(db: Session, expense: Expense) -> None:
    stored_expense = get_expense_id(db=db, expense_id=expense.id)
    assert stored_expense
