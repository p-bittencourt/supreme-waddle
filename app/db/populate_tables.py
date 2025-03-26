from sqlalchemy import insert
from sqlalchemy.orm import Session

from app.db.database import engine
from app.models.user import User
from app.models.expense import Expense
from app.db.data import users, expenses


def populate_users():
    user_objects = [User(**user) for user in users]
    with Session(engine) as session:
        session.begin()
        try:
            session.add_all(user_objects)
        except Exception as e:
            session.rollback()
            print("Oops, something went wrong: " + str(e))
        else:
            session.commit()


def populate_expenses():
    expense_objects = [Expense(**expense) for expense in expenses]
    print(expense_objects)
    with Session(engine) as session:
        session.begin()
        try:
            session.add_all(expense_objects)
        except Exception as e:
            session.rollback()
            print("Oops, something went wrong")
        else:
            session.commit()


# populate_users()
# populate_expenses()
