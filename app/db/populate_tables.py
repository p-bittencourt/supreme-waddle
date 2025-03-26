from sqlalchemy import insert

from app.db.database import Base, engine
from app.models.user import User
from app.models.expense import Expense
from app.schemas.expense import ExpenseCategory
from app.db.data import users, expenses


def populate_users():
    try:
        stmt = insert(User).values(users)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        print(f"Successfully added {result.rowcount} users")
    except Exception as e:
        print("Oops, something went wrong: " + str(e))


def populate_expenses():
    try:
        stmt = insert(Expense).values(expenses)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        print(f"Successfully added {result.rowcount} expenses")
    except Exception as e:
        print("Oops, something went wrong: " + str(e))


# populate_users()
# populate_expenses()
