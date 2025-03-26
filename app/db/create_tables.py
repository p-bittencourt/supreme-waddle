"""This function creates the tables"""

from app.db.database import Base, engine
from app.models.user import User
from app.models.expense import Expense


def create_tables():
    """Creates the tables using the models defined on app.models"""
    try:
        Base.metadata.create_all(bind=engine)
        print("[SUCCESS] Database tables created successfully!")
    except Exception as e:
        print("[ERROR] Something went wrong:", str(e))


if __name__ == "__main__":
    create_tables()
