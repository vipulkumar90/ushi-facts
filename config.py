from pathlib import Path
import os

from dotenv import load_dotenv

# Project root
BASE_DIR = Path(__file__).resolve().parent

# Load local environment variables (if present)
load_dotenv(BASE_DIR / ".env")

# Discord
DISCORD_WEBHOOK_URL: str = os.getenv("DISCORD_WEBHOOK_URL", "")

# Database
SYNC_SEED_DATA: bool = (
    os.getenv("SYNC_SEED_DATA", "false").strip().lower() == "true"
)

# Logging
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()