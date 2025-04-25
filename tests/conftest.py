"""Conftest file to setup test db"""

import logging
from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

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
    with engine.connect() as connection:
        try:
            connection.execute(text(f"CREATE DATABASE {TEST_DB_URI.split('/')[-1]}"))
        except Exception as e:
            logger.error("Issue creating db %s", str(e))


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
    UserFactory._meta.sqlalchemy_session = db
    ExpenseFactory._meta.sqlalchemy_session = db
