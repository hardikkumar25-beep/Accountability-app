from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password:str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at:datetime
