"""Establish endpoints for interacting with expenses"""

from fastapi import APIRouter
from app.schemas.expense import ExpenseResponse, ExpenseUpdate

from app.repositories.expense import *

router = APIRouter(
    prefix="/expenses", tags=["expenses"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[ExpenseResponse], tags=["expenses"])
async def read_expenses():
    return retrieve_expenses()


@router.get("/{expense_id}", response_model=ExpenseResponse, tags=["expenses"])
async def read_expense_id(expense_id: str):
    return retrieve_expense_id(expense_id)


@router.put("/{expense_id}", response_model=ExpenseResponse, tags=["expenses"])
async def update_expense(expense_id: str, expense_update: ExpenseUpdate):
    pass
