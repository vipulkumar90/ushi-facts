from database.initializer import initialize_database
from services.discord_service import DiscordService
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
        discord_service = DiscordService()

        # Retrieve next fact
        fact = fact_service.get_next_fact()

        if fact is None:
            logger.warning("No eligible facts found.")
            return

        logger.info("Selected fact: %s", fact.fact_key)

        discord_service.send_fact(fact)

        logger.info("Discord message sent successfully.")

        fact_service.mark_posted(fact.fact_key)

        logger.info(
            "Updated posting history for '%s'.",
            fact.fact_key,
        )

        logger.info("Application completed successfully.")

    except Exception:
        logger.exception("Application terminated unexpectedly.")
        raise


if __name__ == "__main__":
    main()
