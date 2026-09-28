# Telegram Transcription Bot


> An asynchronous Telegram bot designed to instantly transcribe voice messages into text. Powered by the Groq API (using the Whisper model) and built with Aiogram 3, it offers highly accurate speech-to-text conversion with smart language auto-detection, making it a simple tool for processing voice messages on the go.

---

## ✨ Features

* 🎙️ **High-Speed Transcription:** Instantly converts voice messages to text using the advanced `whisper-large-v3-turbo` model via Groq API.
* 🌍 **Smart Language Detection:** Supports explicit language selection (English, Ukrainian) via inline keyboards, or an "Auto-detect" mode for mixed speech to prevent AI hallucinations.
* ⚡ **Fully Asynchronous:** Built with `aiogram` and `aiosqlite` for non-blocking database operations and high concurrency.
* 🐳 **Docker Ready:** Fast, reliable, and isolated deployment using Docker and Docker Compose (includes persistent volume for the database).
* ⚙️ **Highly Configurable:** No hardcoded constants. Easily switch AI models and API endpoints using `.env` variables.
* 📝 **Text Summarization:** Integrated LLM support to generate quick summaries from long transcriptions.
---

## 🛠 Tech Stack

* **Language:** Python 3.14
* **Framework:** Aiogram 3.30
* **Database:** SQLite (`aiosqlite`)
* **AI API:** Groq (OpenAI-compatible SDK)
* **DevOps:** Docker & Docker Compose
---

## 📦 Prerequisites

Choose your environment:

* **Windows:**
  * [Python](https://www.python.org/downloads) 3.14+ (ensure Python is added to PATH)
  * [Git](https://git-scm.com/)
* **Linux / macOS (Docker):**
  * [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/)
  * [Git](https://git-scm.com/)

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `BOT_TOKEN` | Telegram Bot API token obtained from [@BotFather](https://t.me/BotFather) | *Required* |
| `GROQ_TOKEN` | API key from [Groq Cloud](https://console.groq.com/) | *Required* |
| `GROQ_BASE_URL` | Endpoint for OpenAI-compatible client | `https://api.groq.com/openai/v1` |
| `STT_MODEL` | Speech-to-Text model for voice transcription | `whisper-large-v3-turbo` |
| `LLM_MODEL` | Text model for generating summaries | `openai/gpt-oss-20b` |
| `WINDOW_TIME` | Time window for rate limiting (in seconds)  | `60.0` |
| `RATE_LIMIT` | Maximum requests allowed per time window | `20` |
| `PROMPT_FILE_NAME` | Name of the file containing the system prompt | `instruction.txt` |
---

## Quick Start

### 1. Clone the repository
``` bash
git clone https://github.com/dmitrovskii/transcription-bot
cd transcription-bot
```

### 2. Choose your platform

#### 🪟 Windows (Automatic Setup)
1. **Run the script:** Double-click `run.bat` (or run `run.bat` in CMD/PowerShell)
    * On the first launch, the script will generate a `.env` file and pause.
2. **Add credentials:** Open the newly created `.env` file in any text editor, insert your BOT_TOKEN and GROQ_TOKEN, and save.
3. **Start the bot:** Run `run.bat` again. The script will set up the virtual environment, install requirements, and run the bot.

#### 🐧 Linux / Server (Docker Compose)

1. Setup environment variables:
Copy the example environment file and specify your API tokens:
``` bash
cp .env.example .env
nano .env
```

2. Build and launch:
Build the image and start the container in the background:
``` bash 
docker compose up -d --build 
```

- View logs: `docker compose logs -f`
- Stop bot: `docker compose down`

The bot is now running! Open Telegram, find your bot, and send `/start` to begin.

---

## 👨‍💻 Author & License
* **Author:** @dmitrovskii
* **License:** MIT License