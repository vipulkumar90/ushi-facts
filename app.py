from database.initializer import initialize_database
from services.fact_service import FactService
from utils.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    """
    Application entry point.
    """
    logger.info("=" * 60)
    logger.info("Starting Cow God Facts")

    try:
        # Initialize database
        initialize_database()

        # Create fact service
        fact_service = FactService()

        # Retrieve next fact
        fact = fact_service.get_next_fact()

        if fact is None:
            logger.warning("No fact available to post.")
            return

        logger.info("Fact selected successfully.")

        print("\n" + "=" * 60)
        print(f"Fact Key    : {fact.fact_key}")
        print(f"Category    : {fact.category_en}")
        print(f"Difficulty  : {fact.difficulty}")
        print()
        print("English:")
        print(fact.fact_en)
        print()
        print("Japanese:")
        print(fact.fact_ja)
        print("=" * 60 + "\n")

        # Simulate a successful Discord post
        logger.info("Simulating successful Discord post...")

        fact_service.mark_posted(fact.fact_key)

        logger.info(
            "Fact '%s' marked as posted successfully.",
            fact.fact_key,
        )

        logger.info("Application finished successfully.")

    except Exception:
        logger.exception("Application terminated unexpectedly.")
        raise


if __name__ == "__main__":
    main()