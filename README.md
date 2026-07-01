# 🐄 Ushi  Facts

Ushi Facts is a lightweight Python project that automatically shares bilingual AI facts to Discord.

The project is designed to help readers:

- 🤖 Learn AI concepts
- 🇯🇵 Improve Japanese
- 🇺🇸 Improve English

Facts are stored locally in SQLite and are posted automatically using GitHub Actions, making the project completely serverless and free to host.

---

## Features

- Daily or configurable fact posting
- SQLite database
- Discord Webhook integration
- GitHub Actions automation
- Lightweight (no Discord bot login required)
- Configurable through environment variables
- Designed to support additional topics in the future

---

## Current Topic

- AI

Future topics may include:

- Python
- Programming
- Science
- Mathematics
- Japanese Vocabulary
- Anime
- History

---

## Project Structure

```
ushi-facts/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── data/
│   └── facts.db
│
├── database/
│   ├── db.py
│   └── schema.sql
│
├── models/
│   └── fact.py
│
├── services/
│   ├── discord_service.py
│   └── fact_service.py
│
├── utils/
│   └── logger.py
│
└── .github/
    └── workflows/
        └── post_fact.yml
```

---

## Architecture

```
GitHub Actions
        │
        ▼
app.py
        │
        ▼
Fact Service
        │
        ▼
SQLite Database
        │
        ▼
Discord Webhook
```

---

## Configuration

Environment variables control the application's behavior.

Example:

```
DISCORD_WEBHOOK=

DATABASE_PATH=data/facts.db

TOPIC=AI

POST_MODE=random

POSTS_PER_RUN=1

ALLOW_REPEAT=false

LOG_LEVEL=INFO
```

---

## Database

Facts are stored in SQLite.

Example fields:

- id
- topic
- english
- japanese
- difficulty
- tags
- posted_count
- last_posted
- enabled

---

## Roadmap

### Version 1

- SQLite storage
- Random AI fact
- Discord webhook
- GitHub Actions scheduling

### Version 2

- Multiple topics
- Difficulty filtering
- Rich Discord embeds
- Images
- Categories

### Version 3

- AI-generated facts
- Spaced repetition
- Weekly quizzes
- Topic rotation

---

## Philosophy

Keep it simple.

The bot should only do one thing:

> Select one fact and post it to Discord.

Everything else should be modular and easy to extend.

---

## License

MIT