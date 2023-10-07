import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.token import TokenValidationError
from dotenv import load_dotenv

from bot import handlers

load_dotenv()


logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s, %(levelname)s, %(message)s',
        filemode='w',
        filename='logger.log',
        level=logging.INFO,
    )
    try:
        asyncio.run(main())
    except TokenValidationError:
        raise TokenValidationError('Token is invalid!')
