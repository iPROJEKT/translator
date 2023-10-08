import os

import deepl
from dotenv import load_dotenv

from .const import TARGET_LANG

load_dotenv()

AUTH_KEY = os.getenv('API_TOKEN')
translator = deepl.Translator(AUTH_KEY)


async def translater(text: str) -> str:
    result = translator.translate_text(text, target_lang=TARGET_LANG)
    return result.text
