from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field

class UserCreate(BaseModel):
    username: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    model_config = {"from_attributes": True}
