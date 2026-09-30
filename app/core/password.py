from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from jose import JWTError,jwt
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY", "fallback-insecure-key-for-local-dev-only")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM="HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def create_access_token(data:dict,expires_delta:timedelta |None=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encoded(to_encode,SECRET_KEY,algorithm=[ALGORITHM])
    return encoded_jwt