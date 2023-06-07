### User model ###

from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str] # Puede que no le llegue
    username: str
    email: str