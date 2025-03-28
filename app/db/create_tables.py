"""This function creates the tables"""

from app.db.database import Base, engine

# These models are required for SQLAlchemy to properly create all tables
# even though they appear unised to static analyzers
from app.models.user import User  # pylint: disable=unused-import
from app.models.expense import Expense  # pylint: disable=unused-import


def create_tables():
    """Creates the tables using the models defined on app.models"""
    try:
        Base.metadata.create_all(bind=engine)
        print("[SUCCESS] Database tables created successfully!")
    except Exception as e:
        print("[ERROR] Something went wrong:", str(e))


if __name__ == "__main__":
    create_tables()
