from database.initializer import initialize_database
from database.db import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    logger.info("=" * 60)
    logger.info("Starting Cow God Facts")

    try:
        initialize_database()

        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT *
                FROM facts
                """
            )

            facts = cursor.fetchall()

            logger.info("Database contains %d facts.", len(facts))

            for fact in facts:
                logger.info(
                    "[%s] %s",
                    fact["fact_key"],
                    fact["fact_en"],
                )

        logger.info("Application finished successfully.")

    except Exception:
        logger.exception("Application terminated unexpectedly.")
        raise


if __name__ == "__main__":
    main()