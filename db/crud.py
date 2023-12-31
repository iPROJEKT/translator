from sqlalchemy import select
from aiogram.types import Message

from .db import AsyncSessionLocal
from .models import UserHistory


async def create_user(
        message_data: Message,
        translate_text: str
):
    result = UserHistory(
        user_id=message_data.from_user.id,
        primary_text=message_data.text,
        translate_text=translate_text
    )
    async with AsyncSessionLocal() as session:
        session.add(result)
        await session.commit()
        await session.refresh(result)
    return result


async def get_histiry(
        user_id: int
):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(UserHistory.translate_text).where(
                UserHistory.user_id == user_id
            )
        )
    return result
