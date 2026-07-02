CREATE TABLE IF NOT EXISTS facts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    fact_key        TEXT NOT NULL UNIQUE,

    category_en     TEXT,
    category_ja     TEXT,

    fact_en         TEXT NOT NULL,
    fact_ja         TEXT NOT NULL,

    difficulty      TEXT,

    tags_en         TEXT,
    tags_ja         TEXT,

    posted_count    INTEGER NOT NULL DEFAULT 0,
    last_posted     DATETIME,

    enabled         INTEGER NOT NULL DEFAULT 1,

    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);