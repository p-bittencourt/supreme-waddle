from sqlalchemy.orm import Session

from app.models.expense import ExpenseCategory
from app.schemas.expense import ExpenseCreate
from app.repositories.expense import add_expense
from faker import Faker


def test_add_expense(db: Session) -> None:
    user_id = Faker().rd_number()
    title = Faker().word
    value = Faker().pricetag()
    category = ExpenseCategory.MISCELLANEOUS
    expense_in = ExpenseCreate(
        title=title, value=value, category=category, user_id=user_id
    )
    expense = add_expense(db=db, expense_data=expense_in)
    assert expense.title == title
    assert expense.user_id == user_id
