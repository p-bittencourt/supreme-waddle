"""Define the Models for SQLAlchemy"""

from typing import TYPE_CHECKING, List
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.db.database import Base

if TYPE_CHECKING:
    from app.models.expense import Expense


class User(Base):
    """Define the User Base for SQLAlchemy"""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)

    expenses: Mapped[List["Expense"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
