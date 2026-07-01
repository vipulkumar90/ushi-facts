import json
from pathlib import Path
import sqlite3

from database.db import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
SEED_DIRECTORY = BASE_DIR / "seed"


def synchronize_seed_data() -> None:
    """
    Synchronize all seed JSON files with the database.

    Existing runtime statistics are preserved.
    """
    logger.info("Starting seed synchronization.")

    try:
        seed_files = list(SEED_DIRECTORY.glob("*.json"))

        if not seed_files:
            logger.warning("No seed files found.")
            return

        with get_connection() as connection:

            for seed_file in seed_files:
                logger.info("Processing '%s'.", seed_file.name)

                with seed_file.open("r", encoding="utf-8") as file:
                    facts = json.load(file)

                for fact in facts:
                    _upsert_fact(connection, fact)

            connection.commit()

        logger.info("Seed synchronization completed.")

    except Exception:
        logger.exception("Seed synchronization failed.")
        raise


def _upsert_fact(connection: sqlite3.Connection, fact: dict) -> None:
    """
    Insert a new fact or update editable fields if it already exists.
    """
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id
        FROM facts
        WHERE fact_key = ?
        """,
        (fact["fact_key"],),
    )

    exists = cursor.fetchone()

    if exists:
        logger.debug("Updating %s", fact["fact_key"])

        cursor.execute(
            """
            UPDATE facts
            SET
                category_en=?,
                category_ja=?,
                fact_en=?,
                fact_ja=?,
                difficulty=?,
                tags_en=?,
                tags_ja=?,
                enabled=?,
                updated_at=CURRENT_TIMESTAMP
            WHERE fact_key=?
            """,
            (
                fact["category_en"],
                fact["category_ja"],
                fact["fact_en"],
                fact["fact_ja"],
                fact["difficulty"],
                fact["tags_en"],
                fact["tags_ja"],
                int(fact["enabled"]),
                fact["fact_key"],
            ),
        )

    else:
        logger.debug("Inserting %s", fact["fact_key"])

        cursor.execute(
            """
            INSERT INTO facts (
                fact_key,
                category_en,
                category_ja,
                fact_en,
                fact_ja,
                difficulty,
                tags_en,
                tags_ja,
                enabled
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                fact["fact_key"],
                fact["category_en"],
                fact["category_ja"],
                fact["fact_en"],
                fact["fact_ja"],
                fact["difficulty"],
                fact["tags_en"],
                fact["tags_ja"],
                int(fact["enabled"]),
            ),
        )