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
# Discord
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your-webhook-url

# Database
SYNC_SEED_DATA=false

# Logging
LOG_LEVEL=INFO

# Fact Selection
FACT_SELECTION_STRATEGY=random
ALLOW_REPEAT=false
DEFAULT_CATEGORY=AI

# Database
DATABASE_PROVIDER=sqlite

# SQLite
SQLITE_DATABASE_PATH=data/facts.db

# Supabase PostgreSQL
POSTGRES_HOST=
POSTGRES_PORT=5432
POSTGRES_DATABASE=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_SSLMODE=require
```

---

## How to Use

You can run Ushi Facts either locally on your own machine or automatically using GitHub Actions.

### Run Locally

#### Prerequisites

* Python 3.10 or later
* Discord Webhook URL
* Git (optional if downloading the project as a ZIP)

#### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ushi-facts.git
cd ushi-facts
```

Or download the repository as a ZIP and extract it.

#### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure environment variables

Copy the example configuration file:

```bash
cp .env.example .env
```

If you're using Windows Command Prompt:

```cmd
copy .env.example .env
```

Open `.env` and configure at least:

* `DISCORD_WEBHOOK_URL`
* Any other settings you wish to customize

#### 5. Run the application

```bash
python app.py
```

The application will:

* Create the SQLite database automatically (if it doesn't exist).
* Synchronize seed data if enabled.
* Select the next fact.
* Send it to Discord.
* Update the posting history.

---

### Run with GitHub Actions

If you'd like to run the bot automatically every day without keeping your computer on:

#### 1. Fork this repository

Click **Fork** on GitHub to create your own copy.

#### 2. Configure GitHub Secrets

Go to:

**Repository → Settings → Secrets and variables → Actions**

Add the required secrets (for example):

* `DISCORD_WEBHOOK_URL`
* Any additional secrets required by your deployment

#### 3. Enable GitHub Actions

The included workflow will automatically run according to the configured cron schedule.

You can also trigger it manually from the **Actions** tab using **Run workflow**.

Once configured, GitHub Actions will automatically execute the bot and post facts to your Discord server on the configured schedule.

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
