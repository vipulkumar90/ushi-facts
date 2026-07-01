CREATE TABLE IF NOT EXISTS facts (
    id              SERIAL PRIMARY KEY,

    fact_key        TEXT UNIQUE NOT NULL,

    category_en     TEXT,
    category_ja     TEXT,

    fact_en         TEXT NOT NULL,
    fact_ja         TEXT NOT NULL,

    difficulty      TEXT,

    tags_en         TEXT,
    tags_ja         TEXT,

    posted_count    INTEGER NOT NULL DEFAULT 0,
    last_posted     TIMESTAMP,

    enabled         BOOLEAN NOT NULL DEFAULT TRUE,

    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);