from fastapi import FastAPI
from app.routes import users, expenses

app = FastAPI(
    title="Expense Tracker API",
    description="An exercise for learning FastAPI and PostgreSQL",
    version="0.1.0",
)


app.include_router(users.router)
app.include_router(expenses.router)


@app.get("/")
def root():
    return {"message": "Welcome to PB's Expense Tracker"}
