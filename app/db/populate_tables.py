"""Functions for populating the database after tables have been created"""

from sqlalchemy.orm import Session

from app.db.database import engine
from app.models.user import User
from app.models.expense import Expense
from app.db.data import users, expenses


def populate_users():
    """Populates the db with users"""
    user_objects = [User(**user) for user in users]
    with Session(engine) as session:
        session.begin()
        try:
            session.add_all(user_objects)
        except:
            session.rollback()
        else:
            session.commit()


def populate_expenses():
    """Populates the db with expenses"""
    expense_objects = [Expense(**expense) for expense in expenses]
    print(expense_objects)
    with Session(engine) as session:
        session.begin()
        try:
            session.add_all(expense_objects)
        except:
            session.rollback()
        else:
            session.commit()


if __name__ == "__main__":
    populate_users()
    populate_expenses()
