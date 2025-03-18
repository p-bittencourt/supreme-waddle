from app.db.database import Base, engine
from app.models.user import User
from app.models.expense import Expense


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")


if __name__ == "__main__":
    create_tables()
