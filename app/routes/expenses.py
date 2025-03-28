"""Establish endpoints for interacting with expenses"""

from fastapi import APIRouter
from app.schemas.expense import ExpenseResponse, ExpenseUpdate

from app.repositories.expense import *
from app.db.database import DbSession

router = APIRouter(
    prefix="/expenses", tags=["expenses"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[ExpenseResponse], tags=["expenses"])
async def read_expenses(db: DbSession):
    """Retrieve all expenses."""
    return retrieve_expenses(db)


@router.get("/{expense_id}", response_model=ExpenseResponse, tags=["expenses"])
async def read_expense_id(db: DbSession, expense_id: str):
    """Retrieve a specific expense by its ID."""
    return retrieve_expense_id(db, expense_id)


@router.put("/{expense_id}", response_model=ExpenseResponse, tags=["expenses"])
async def update_expense(db: DbSession, expense_id: str, expense_update: ExpenseUpdate):
    """Update an expense by its ID."""
    pass
