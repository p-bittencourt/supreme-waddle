from typing import TYPE_CHECKING, get_args
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.schemas.expense import ExpenseCategory
from app.db.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

if TYPE_CHECKING:
    from app.models.user import User


class Expense(Base):
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
