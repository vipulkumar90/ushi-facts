# services/discord_service.py

import requests

from config import DISCORD_WEBHOOK_URL
from models.fact import Fact
from utils.logger import get_logger

logger = get_logger(__name__)


class DiscordService:
    """
    Service responsible for sending facts to Discord via webhook.
    """

    EMBED_COLOR = 0xF1C40F  # Warm gold

    def send_fact(self, fact: Fact) -> None:
        """
        Send a fact to Discord.

        Raises:
            ValueError: If the webhook URL is missing.
            requests.RequestException: If the request fails.
        """
        logger.info("Sending fact '%s' to Discord.", fact.fact_key)

        if not DISCORD_WEBHOOK_URL:
            logger.error("Discord webhook URL is not configured.")
            raise ValueError("Discord webhook URL is missing.")

        payload = self._build_payload(fact)

        try:
            response = requests.post(
                DISCORD_WEBHOOK_URL,
                json=payload,
                timeout=10,
            )

            response.raise_for_status()

            logger.info(
                "Successfully sent fact '%s' to Discord.",
                fact.fact_key,
            )

        except requests.Timeout:
            logger.exception("Discord request timed out.")
            raise

        except requests.ConnectionError:
            logger.exception("Failed to connect to Discord.")
            raise

        except requests.HTTPError:
            logger.error(
                "Discord returned HTTP %s: %s",
                response.status_code,
                response.text,
            )
            raise

        except requests.RequestException:
            logger.exception("Unexpected Discord request error.")
            raise

    def _build_payload(self, fact: Fact) -> dict:
        """
        Build the Discord webhook payload.
        """

        tags = ""

        if fact.tags_en:
            tags = " • ".join(
                tag.strip() for tag in fact.tags_en.split(",") if tag.strip()
            )

        embed = {
            "title": "🐄 牛神のお告げ",
            "description": ("*A little wisdom from the Cow God.*"),
            "color": self.EMBED_COLOR,
            "fields": [
                {
                    "name": "📚 Category",
                    "value": f"{fact.category_ja}\n*{fact.category_en}*",
                    "inline": False,
                },
                {
                    "name": "🇯🇵 日本語",
                    "value": fact.fact_ja,
                    "inline": False,
                },
                {
                    "name": "🇺🇸 English",
                    "value": fact.fact_en,
                    "inline": False,
                },
            ],
            "footer": {"text": f"Difficulty • {fact.difficulty}"},
        }

        if tags:
            embed["fields"].append(
                {
                    "name": "🏷️ Tags",
                    "value": tags,
                    "inline": False,
                }
            )

        return {
            "embeds": [embed],
        }
