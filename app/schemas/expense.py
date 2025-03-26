"""Pydantic schemas for data validation"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ExpenseCategory(Enum):
    """Possible categories for expenses"""

    GROCERIES = "GROCERIES"
    HEALTH = "HEALTH"
    HOUSING = "HOUSING"
    TRANSPORTATION = "TRANSPORTATION"
    UTILITIES = "UTILITIES"
    ENTERTAINMENT = "ENTERTAINMENT"
    DINING = "DINING"
    EDUCATION = "EDUCATION"
    CLOTHING = "CLOTHING"
    PERSONAL = "PERSONAL"
    TRAVEL = "TRAVEL"
    INSURANCE = "INSURANCE"
    SAVINGS = "SAVINGS"
    GIFTS = "GIFTS"
    SUBSCRIPTIONS = "SUBSCRIPTIONS"
    MISCELLANEOUS = "MISCELLANEOUS"


class ExpenseBase(BaseModel):
    """Base expense model with common attributes"""

    title: str = Field(min_length=1)
    category: ExpenseCategory
    value: float = Field(gt=0)


class ExpenseCreate(ExpenseBase):
    """Used when creating a new expense (no ID yet)"""

    user_id: int


class ExpenseUpdate(BaseModel):
    """Used when updating an expense (all fields optional)"""

    title: Optional[str] = Field(None, min_length=1)
    category: Optional[ExpenseCategory] = None
    value: Optional[float] = Field(None, gt=0)


class ExpenseResponse(ExpenseBase):
    """Full expense model returned to clients"""

    id: int
    user_id: int

    class Config:
        """Configuration for response serialization.

        The from_attributes=True setting allows the model to read data from
        SQLAlchemy ORM models, converting model attributes to schema fields.
        """

        from_attributes = True
