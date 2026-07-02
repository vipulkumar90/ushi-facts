from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Fact:
    """
    Represents a fact stored in the SQLite database.
    """

    id: int
    fact_key: str

    category_en: str
    category_ja: str

    fact_en: str
    fact_ja: str

    difficulty: str

    tags_en: str
    tags_ja: str

    posted_count: int
    last_posted: datetime | None

    enabled: bool

    created_at: datetime
    updated_at: datetime
