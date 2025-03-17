from pydantic import BaseModel


class Expense(BaseModel):
    id: int
    user_id: int
    title: int
    category: str
    value: int
