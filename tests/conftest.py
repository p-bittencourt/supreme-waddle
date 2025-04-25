# pylint: disable=W0621
"""Conftest file to setup test db"""

import logging
from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

# Import dependency that needs to be overridden
from app.db.database import get_db
from app.main import app
from app.core.config import Settings
from app.db.database import Base, engine
from app.models.user import User  # pylint: disable=unused-import
from app.models.expense import Expense  # pylint: disable=unused-import

from .factories.user import UserFactory
from .factories.expense import ExpenseFactory


# Set up a test Database
TEST_DB_URI = Settings.TEST_DB_URI
engine = create_engine(TEST_DB_URI)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = logging.getLogger(__name__)


def create_test_database():
    """Create the test database if it doesn't exist"""
    # Get the database name from the TEST_DB_URI
    db_name = Settings.TEST_DB

    # Create a connection string to the default postgres database
    postgres_uri = f"postgresql://{Settings.DB_USER}:{Settings.DB_PASSWORD}@{Settings.DB_HOST}:{Settings.DB_PORT}/postgres"  # pylint: disable=line-too-long

    # Create engine with autocommit=True to allow CREATE DATABASE
    temp_engine = create_engine(postgres_uri, isolation_level="AUTOCOMMIT")

    try:
        # Connect to the postgres database
        with temp_engine.connect() as connection:
            # Check if our test database already exists
            result = connection.execute(
                text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
            )

            if not result.scalar():
                # Create the test database if it doesn't exist
                logger.info("Creating test database: %s", db_name)
                connection.execute(text(f'CREATE DATABASE "{db_name}"'))
                logger.info("Test database %s created successfully", db_name)
            else:
                logger.info("Test database %s already exists", db_name)
    except Exception as e:
        logger.error("Error creating test database: %s", str(e))
        raise


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """
    Create the test database schema before any tests run,
    and drop it after all tests are done.
    """
    create_test_database()
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db() -> Generator:
    """
    Create a new database session for each test and roll it back after the test.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(autouse=True)
def set_session_for_factories(db: Session):
    """Attaches the mock session to the factories"""
    UserFactory._meta.sqlalchemy_session = db
    ExpenseFactory._meta.sqlalchemy_session = db


@pytest.fixture
def expense(db: Session) -> Expense:
    """Create a test expense for use in tests"""
    return ExpenseFactory()


@pytest.fixture(scope="function")
def client(db: Session) -> Generator[TestClient, None, None]:
    """Overrides database dependency"""

    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
