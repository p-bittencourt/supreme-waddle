"""Creating the db engine"""

from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from app.core.config import Settings


engine = create_engine(Settings.DATABASE_URL)

SessionLocal = sessionmaker(engine)


def get_db():
    """Instantiates the session and yield it as a dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]


class Base(DeclarativeBase):
    """Declarative Base to be reused in other Classes"""

    pass
