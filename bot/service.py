from collections import deque
import time
from pathlib import Path
import logging 
from typing import Any 

from aiogram import Bot
from openai import AsyncOpenAI

from config import config

logger = logging.getLogger(__name__)

timestamps = deque()

PROMPT_FILE = Path(__file__).resolve().parent / config.prompt_file_name

DEFAULT_INSTRUCTION = (
"""
You are a text summarizer. Summarize the input text according to these strict rules: 
1. LANGUAGE MATCH: You MUST respond in the EXACT same language as the input text (e.g., Russian input -> Russian output; Ukrainian input -> Ukrainian output). 
2. LENGTH: Maximum 4-5 sentences or plain text bullet points. 
3. FORMATTING: Plain text ONLY. Do NOT use any Markdown (no asterisks *, no hashes #, no bolding). 
4. CONCISENESS: Extract only the core message. Eliminate all filler and fluff. 
5. PERSPECTIVE: Write strictly in the third person (refer to the author/speaker neutrally). NEVER address anyone in the second person ("you", "ты", "ти", etc.).
"""    
)

def get_system_prompt() -> str:
    if not PROMPT_FILE.exists():
        logger.warning(f"File {PROMPT_FILE} not found. Creating with default prompt.")
        PROMPT_FILE.write_text(DEFAULT_INSTRUCTION, encoding="utf-8")
        return DEFAULT_INSTRUCTION
    return PROMPT_FILE.read_text(encoding="utf-8").strip()



groq_client = AsyncOpenAI(
    base_url=config.groq_base_url,
    api_key=config.groq_token
)

async def process_voice(file_id: str, language_code: str, bot: Bot) -> dict[str, str | Any]:
    now = time.monotonic()

    while timestamps and timestamps[0] < now - config.window_time:
        timestamps.popleft()

    if len(timestamps) < config.rate_limit:
        timestamps.append(now)

        file = await bot.download(file=file_id)

        params = {
            "file": ("voice.ogg", file.read()),  # type: ignore
            "model": config.stt_model,
            "response_format": "text",
        }

        if language_code and language_code != "auto":
            params["language"] = language_code

        message = await groq_client.audio.transcriptions.create(**params)

    else:
        message = "Too many requests. Try again later."

    return {"message": message}

async def process_text(transcribed_text: str) -> dict[str, Any]:
    response = await groq_client.chat.completions.create(
        model=config.llm_model,
        messages=[
            {
                "role": "assistant",
                "content": get_system_prompt()
            },
            {
                "role": "user", "content": transcribed_text
            }
        ],
        temperature=0.3
    )
    return {"message": response.choices[0].message.content}