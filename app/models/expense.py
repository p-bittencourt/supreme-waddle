from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.schemas.expense import ExpenseCategory
from app.db.database import Base

if TYPE_CHECKING:
    from app.models.user import User


class Expense(Base):
    """Define the Expense Base for SQLAlchemy"""

    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[ExpenseCategory] = mapped_column(
        Enum(ExpenseCategory, name="expensecategory"),
        nullable=False,
    )
    value: Mapped[float] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="expenses")

    def __repr__(self) -> str:
        return (
            f"Expense(id={self.id}, "
            f"title='{self.title}', "
            f"category='{self.category}', "
            f"value='{self.value}')"
        )
