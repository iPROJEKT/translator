from sqlalchemy import Column, Integer, BigInteger, String
from aiogram import types

from db.base import Base, session


class UserHistory(Base):
    __tablename__ = 'userhistory'
    id = Column(
        Integer,
        primary_key=True
    )
    user_id = Column(
        BigInteger,
        unique=True,
    )
    message_inp = Column(
        String,
    )
    message_out = Column(
        String,
    )

    @staticmethod
    async def save(msg: types.Message, text: str) -> None:
        user_message = UserHistory(
            user_id=msg.from_user.id,
            message_inp=msg.text,
            message_out=text
        )
        session.add(user_message)
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise Exception

    @staticmethod
    async def get_histori(msg):
        return session.query(UserHistory).filter(UserHistory.id == msg.from_user.id)
