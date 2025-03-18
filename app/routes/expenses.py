from fastapi import APIRouter, HTTPException
from app.schemas.expense import ExpenseCategory, ExpenseResponse, ExpenseUpdate


router = APIRouter(
    prefix="/expenses", tags=["expenses"], responses={404: {"description": "Not found"}}
)

fake_expenses_db = [
    {
        "id": 1,
        "title": "Apples and Oranges",
        "category": ExpenseCategory.GROCERIES.value,  # Use .value to get the string
        "value": 8.76,
        "user_id": 1,
    },
    {
        "id": 2,
        "title": "Internet bill",
        "category": ExpenseCategory.UTILITIES.value,
        "value": 89.90,
        "user_id": 1,
    },
    {
        "id": 3,
        "title": "Movie tickets",
        "category": ExpenseCategory.ENTERTAINMENT.value,
        "value": 24.00,
        "user_id": 2,
    },
]


@router.get("/", response_model=list[ExpenseResponse])
def read_expenses():
    return fake_expenses_db


@router.get("/{expense_id}", response_model=ExpenseResponse)
def read_expense(expense_id: int):
    for expense in fake_expenses_db:
        if expense["id"] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")


@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, expense_update: ExpenseUpdate):
    pass
