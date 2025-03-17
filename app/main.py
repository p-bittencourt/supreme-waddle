from fastapi import FastAPI
from app.schemas import Expense, User

app = FastAPI(
    title="Expense Tracker API",
    description="An exercise for learning FastAPI and PostgreSQL",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to PB's Expense Tracker"}
