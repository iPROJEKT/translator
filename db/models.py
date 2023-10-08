from sqlalchemy import Column, String, Integer

from .db import Base


class UserHistory(Base):
    user_id = Column(
        Integer(),
        nullable=False
    )
    primary_text = Column(
        String(),
        nullable=False
    )
    translate_text = Column(
        String(),
        nullable=False
    )
