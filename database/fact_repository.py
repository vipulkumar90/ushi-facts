import random
import sqlite3

from database.db import get_connection
from models.fact import Fact
from utils.logger import get_logger

logger = get_logger(__name__)


class FactRepository:
    """
    Handles all database operations related to facts.
    """

    def get_random_fact(
        self,
        categories: list[str],
        allow_repeat: bool,
    ) -> Fact | None:
        """
        Retrieve a random eligible fact.
        """
        logger.info("Fetching random fact.")

        try:
            query = """
                SELECT *
                FROM facts
                WHERE enabled = 1
            """

            parameters: list = []

            if categories:
                placeholders = ",".join("?" * len(categories))
                query += f" AND category_en IN ({placeholders})"
                parameters.extend(categories)

            if not allow_repeat:
                query += " AND posted_count = 0"

            query += """
                ORDER BY RANDOM()
                LIMIT 1
            """

            with get_connection() as connection:
                cursor = connection.execute(query, parameters)

                row = cursor.fetchone()

            if row is None:
                logger.warning("No eligible facts found.")
                return None

            fact = self._row_to_fact(row)

            logger.info("Selected fact '%s'.", fact.fact_key)

            return fact

        except sqlite3.Error:
            logger.exception("Failed to retrieve fact.")
            raise

    def mark_fact_posted(self, fact_key: str) -> None:
        """
        Update posting statistics after a successful post.
        """
        logger.info("Updating posting history for '%s'.", fact_key)

        try:
            with get_connection() as connection:
                connection.execute(
                    """
                    UPDATE facts
                    SET
                        posted_count = posted_count + 1,
                        last_posted = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE fact_key = ?
                    """,
                    (fact_key,),
                )

                connection.commit()

            logger.info("Posting history updated.")

        except sqlite3.Error:
            logger.exception("Failed to update posting history.")
            raise

    @staticmethod
    def _row_to_fact(row: sqlite3.Row) -> Fact:
        """
        Convert a SQLite row into a Fact object.
        """
        return Fact(
            id=row["id"],
            fact_key=row["fact_key"],
            category_en=row["category_en"],
            category_ja=row["category_ja"],
            fact_en=row["fact_en"],
            fact_ja=row["fact_ja"],
            difficulty=row["difficulty"],
            tags_en=row["tags_en"],
            tags_ja=row["tags_ja"],
            posted_count=row["posted_count"],
            last_posted=row["last_posted"],
            enabled=bool(row["enabled"]),
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )