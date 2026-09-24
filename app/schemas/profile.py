from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime

class ProfileCreate(BaseModel):
    plan_description:str

class ProfileResponse(BaseModel):
    id:int
    user_id:int
    plan_description:str

class ProfileUpdate(BaseModel):
    plan_description:str | None =None