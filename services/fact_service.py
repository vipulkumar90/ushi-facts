from database.fact_repository import FactRepository
from models.fact import Fact
from config import (
    ALLOW_REPEAT,
    DEFAULT_CATEGORIES,
    FACT_SELECTION_STRATEGY,
)
from utils.logger import get_logger

logger = get_logger(__name__)


class FactService:
    """
    Business logic for retrieving and updating facts.
    """

    def __init__(self, repository: FactRepository | None = None) -> None:
        self._repository = repository or FactRepository()

    def get_next_fact(self) -> Fact | None:
        """
        Retrieve the next fact according to the configured strategy.

        Returns:
            Fact if one is available, otherwise None.
        """
        logger.info("Selecting next fact.")

        logger.debug(
            "Strategy=%s | Categories=%s | Allow Repeat=%s",
            FACT_SELECTION_STRATEGY,
            DEFAULT_CATEGORIES,
            ALLOW_REPEAT,
        )

        try:
            if FACT_SELECTION_STRATEGY != "random":
                logger.warning(
                    "Unsupported strategy '%s'. Falling back to random.",
                    FACT_SELECTION_STRATEGY,
                )

            fact = self._repository.get_random_fact(
                categories=DEFAULT_CATEGORIES,
                allow_repeat=ALLOW_REPEAT,
            )

            if fact is None:
                logger.warning("No eligible facts available.")
                return None

            logger.info("Selected fact '%s'.", fact.fact_key)

            return fact

        except Exception:
            logger.exception("Failed to retrieve next fact.")
            raise

    def mark_posted(self, fact_key: str) -> None:
        """
        Update posting statistics after a successful Discord post.
        """
        logger.info("Marking fact '%s' as posted.", fact_key)

        try:
            self._repository.mark_fact_posted(fact_key)

            logger.info("Fact '%s' marked as posted.", fact_key)

        except Exception:
            logger.exception(
                "Failed to update posting history for '%s'.",
                fact_key,
            )
            raise