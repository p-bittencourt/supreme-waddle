"""Test script for Expense crud operations"""

from pydantic import ValidationError
import pytest
from sqlalchemy.orm import Session

from app.exceptions import NotFound
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


def test_expense_create_bad_request(db: Session) -> None:
    """Tests adding an expense with wrong data types"""
    user = UserFactory()

    title = ""  # empty
    value = 1234  # wrong data type
    category = ""  # shouldn't be empty

    with pytest.raises(ValidationError):
        ExpenseCreate(title=title, value=value, category=category, user_id=user.id)


def test_get_expense(db: Session, expense: Expense) -> None:
    """Testes retrieving an expense"""
    stored_expense = get_expense_id(db=db, expense_id=expense.id)
    assert stored_expense


def test_get_expense_not_found(db: Session) -> None:
    """Tests looking for an non-existing expense"""
    with pytest.raises(NotFound):
        get_expense_id(db=db, expense_id="223344")
