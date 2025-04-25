"""Manages all environment variables"""

import os
from dotenv import load_dotenv


class Settings:
    """Import all environment variables into Settings class"""

    load_dotenv()
    # Extract database connection parameters from environment variables
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    # Construct the database URL
    DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@" f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    TEST_DB = DB_NAME + "_test"
    TEST_DB_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@" f"{DB_HOST}:{DB_PORT}/{TEST_DB}"
    )
