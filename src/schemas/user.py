from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: Optional[str] = None

class UserCreateRequest(BaseModel):
    name: str
    job: str

class UserCreateResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str