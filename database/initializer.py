# database/initializer.py

from pathlib import Path

from config import SYNC_SEED_DATA
from database.db import database_exists, get_connection
from database.seed_sync import synchronize_seed_data
from utils.logger import get_logger

logger = get_logger(__name__)

SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def initialize_database() -> None:
    """
    Initialize the application's SQLite database.

    Startup behavior:
    1. Create the database if it does not exist.
    2. Create all required tables.
    3. Seed the database from JSON files.
    4. Optionally synchronize seed data when SYNC_SEED_DATA=True.
    """
    try:
        if not database_exists():
            logger.info("Database not found. Creating a new database.")

            _create_schema()

            logger.info("Performing initial seed synchronization.")
            synchronize_seed_data()

            logger.info("Database initialized successfully.")

        elif SYNC_SEED_DATA:
            logger.info("SYNC_SEED_DATA enabled. Synchronizing seed data.")

            synchronize_seed_data()

            logger.info("Seed synchronization completed.")

        else:
            logger.info("Using existing database.")

    except Exception:
        logger.exception("Database initialization failed.")
        raise


def _create_schema() -> None:
    """
    Execute the database schema SQL script.
    """
    try:
        logger.info("Creating database schema.")

        with get_connection() as connection:
            schema = SCHEMA_PATH.read_text(encoding="utf-8")

            connection.executescript(schema)
            connection.commit()

        logger.info("Database schema created successfully.")

    except Exception:
        logger.exception("Failed to create database schema.")
        raise