# Expense Tracker API

A robust REST API built with FastAPI and PostgreSQL for tracking personal expenses. This project demonstrates modern backend development practices including containerization, database integration, and clean code architecture.

## Features

- **User Management**: Create, read, update, and delete user profiles
- **Expense Tracking**: Log and categorize expenses with comprehensive filtering
- **RESTful Design**: Well-structured API endpoints following REST principles
- **Data Validation**: Complete request/response validation using Pydantic schemas
- **Categorized Expenses**: Support for 16 expense categories (Groceries, Health, Travel, etc.)
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Containerized Development**: Docker and Docker Compose configuration for consistent development environments
- **Error Handling**: Custom exceptions with appropriate HTTP status codes
- **Logging**: Comprehensive logging with configurable log levels using Rich for enhanced output
- **API Documentation**: Auto-generated Swagger/OpenAPI documentation
- **CI/CD**: GitHub Actions workflows for code quality and Docker build validation

## Technology Stack

- **Backend Framework**: FastAPI (Python)
- **Database**: PostgreSQL 17
- **ORM**: SQLAlchemy
- **Containerization**: Docker & Docker Compose
- **Validation**: Pydantic
- **Logging**: Rich logging handler
- **Environment Management**: python-dotenv for configuration
- **CI/CD**: GitHub Actions

## API Endpoints

### Users

- `GET /api/users`: Retrieve all users
- `GET /api/users/{user_id}`: Get a specific user by ID
- `POST /api/users`: Create a new user
- `PATCH /api/users/{user_id}`: Update a user
- `DELETE /api/users/{user_id}`: Delete a user

### Expenses

- `GET /api/expenses`: Retrieve expenses (with optional user_id and category filters)
- `GET /api/expenses/{expense_id}`: Get a specific expense by ID
- `POST /api/expenses`: Create a new expense
- `PATCH /api/expenses/{expense_id}`: Update an expense
- `DELETE /api/expenses/{expense_id}`: Delete an expense

## Project Structure

```
/app
├── db
│   └── database.py  # Database connection and session management
├── models           # SQLAlchemy ORM models
│   ├── expense.py
│   └── user.py
├── repositories     # Database interaction logic
│   ├── expense.py
│   └── user.py
├── routes           # API endpoints
│   ├── expenses.py
│   └── users.py
├── schemas          # Pydantic models for request/response validation
│   ├── expense.py
│   └── user.py
├── exceptions.py    # Custom exception handling
├── logging.py       # Logging configuration
└── main.py          # Application entry point
```

## Running the Project

### Prerequisites

- Docker and Docker Compose
- Python 3.9+
- PostgreSQL (if running locally)

### Environment Setup

Create a `.env` file with the following variables:

```
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
DB_NAME=your_db_name
```

### Running with Docker Compose

```bash
# Start the containers
docker-compose up -d

# The API will be available at http://localhost:8080
# API documentation available at http://localhost:8080/docs
```

### Database Initialization

For first-time setup, you need to create the database tables and populate them with initial data:

```bash
# Create tables
python -m app.create_tables

# Populate tables with sample data (optional)
python -m app.populate_tables
```

### Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

## CI/CD Pipelines

The project includes several GitHub Actions workflows:

### Code Quality

- **Pylint**: Automatically runs on pull requests to check code quality for Python 3.9 and 3.10
  - Ensures code adheres to Python best practices and style guidelines

### Docker Builds

- **CI Docker**: Validates Docker build setup on pull requests to the `develop` branch
  - Sets up Docker Buildx for multi-platform builds
- **CD Docker**: Validates Docker image builds on pull requests to the `main` branch
  - Checks out the repository
  - Authenticates with Docker Hub
  - Builds the Docker image (without pushing)

These workflows help maintain code quality and ensure that the application can be properly containerized before merging changes into the main branches.

## Development Skills Demonstrated

- **API Development**: Building a RESTful API with FastAPI
- **Database Design**: Relational database modeling with PostgreSQL
- **ORM Implementation**: Using SQLAlchemy for database interactions
- **Data Validation**: Request/response validation with Pydantic
- **Error Handling**: Custom exceptions with appropriate HTTP status codes
- **Containerization**: Docker and Docker Compose for development environments
- **Backend Architecture**: Clean separation of concerns (routes, repositories, models)
- **Documentation**: Self-documenting API with OpenAPI/Swagger
- **Environment Management**: Using dotenv for configuration
- **Logging**: Structured logging with configurable levels
- **CI/CD**: Automated pipelines for code quality and build validation
- **Version Control**: Git branch management with protected branches

## Future Enhancements

- Add authentication and authorization
- Implement pagination for list endpoints
- Add testing with pytest
- Include statistics and reporting features
- Expand CI/CD with automated deployment and testing
