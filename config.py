import os
from pathlib import Path

from dotenv import load_dotenv

# Project root
BASE_DIR = Path(__file__).resolve().parent

# Load local environment variables
load_dotenv(BASE_DIR / ".env")

# Discord
DISCORD_WEBHOOK_URL: str = os.getenv("DISCORD_WEBHOOK_URL", "")

# Database
SYNC_SEED_DATA: bool = os.getenv("SYNC_SEED_DATA", "false").strip().lower() == "true"

# Logging
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()

# Fact Selection
FACT_SELECTION_STRATEGY: str = (
    os.getenv(
        "FACT_SELECTION_STRATEGY",
        "random",
    )
    .strip()
    .lower()
)

ALLOW_REPEAT: bool = os.getenv("ALLOW_REPEAT", "false").strip().lower() == "true"

DEFAULT_CATEGORIES: list[str] = [
    category.strip()
    for category in os.getenv("DEFAULT_CATEGORY", "AI").split(",")
    if category.strip()
]

# Database Provider
DATABASE_PROVIDER = (
    os.getenv(
        "DATABASE_PROVIDER",
        "sqlite",
    )
    .strip()
    .lower()
)

# SQLite
SQLITE_DATABASE_PATH = os.getenv(
    "SQLITE_DATABASE_PATH",
    "data/facts.db",
)

# PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "")
POSTGRES_USER = os.getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_SSLMODE = os.getenv(
    "POSTGRES_SSLMODE",
    "require",
)
