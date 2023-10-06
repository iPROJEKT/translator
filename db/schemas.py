from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    description: Optional[str]
