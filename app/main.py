from fastapi import APIRouter, FastAPI
from fastapi.responses import RedirectResponse
from app.routes import users, expenses

app = FastAPI(
    title="Expense Tracker API",
    description="An exercise for learning FastAPI and PostgreSQL",
    version="0.1.0",
)

api_router = APIRouter(prefix="/api")


@api_router.get("/", tags=["api"])
def api_root():
    return {
        "message": "Welcome to PB's Expense Tracker API",
        "available_routes": ["/api/users", "/api/expenses"],
    }


api_router.include_router(users.router)
api_router.include_router(expenses.router)


app.include_router(api_router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
