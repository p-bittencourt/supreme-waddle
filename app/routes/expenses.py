"""Establish endpoints for interacting with expenses"""

from fastapi import APIRouter

from app.db.database import DbSession
from app.schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate
import app.repositories.expense as expense_repository

router = APIRouter(
    prefix="/expenses", tags=["expenses"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[ExpenseResponse])
async def read_expenses(db: DbSession, user_id: str = None, category: str = None):
    """
    Retrieve expenses with optional filtering.

    - Filter by user_id
    - Filter by expense category
    - Filter by both
    - Or get all expenses with no filters
    """
    return expense_repository.get_filtered_expenses(db, user_id, category)


@router.get("/{expense_id}", response_model=ExpenseResponse)
async def read_expense_id(db: DbSession, expense_id: str):
    """Retrieve a specific expense by its ID."""
    return expense_repository.get_expense_id(db, expense_id)


@router.patch("/{expense_id}", response_model=ExpenseResponse)
async def update_expense_info(
    db: DbSession, expense_id: str, expense_data: ExpenseUpdate
):
    """Update an expense by its ID."""
    return expense_repository.update_expense(db, expense_id, expense_data)


@router.post("/", response_model=ExpenseResponse)
async def create_expense(db: DbSession, expense_data: ExpenseCreate):
    """Creates an expense"""
    return expense_repository.add_expense(db, expense_data)


@router.delete("/{expense_id}")
async def delete_expense_data(db: DbSession, expense_id: str):
    """Deletes an expense"""
    return expense_repository.delete_expense(db, expense_id)
