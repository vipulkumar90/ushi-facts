# database/db.py

import sqlite3
from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "facts.db"


def database_exists() -> bool:
    """
    Check whether the SQLite database already exists.
    """
    exists = DATABASE_PATH.exists()

    if exists:
        logger.debug("Database found at '%s'.", DATABASE_PATH)
    else:
        logger.debug("Database does not exist.")

    return exists


def get_connection() -> sqlite3.Connection:
    """
    Create and return a SQLite database connection.
    """
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        connection = sqlite3.connect(DATABASE_PATH)
        connection.row_factory = sqlite3.Row

        logger.debug("Connected to SQLite database.")

        return connection

    except sqlite3.Error:
        logger.exception("Failed to connect to the SQLite database.")
        raise
