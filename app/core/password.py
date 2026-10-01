from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from ..database.models.ref_toek import RefreshToken
import jwt
from dotenv import load_dotenv
import os
import bcrypt
import secrets
import hashlib
import uuid
load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY", "fallback-insecure-key-for-local-dev-only")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM="HS256"

def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def create_access_token(data:dict,expires_delta:timedelta |None=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token():
    return secrets.token_urlsafe(64)

def hash_refresh_token(token: str):
    return hashlib.sha256(token.encode()).hexdigest()

def create_refresh_tok_record(db,user_id:int):
    raw_token=create_refresh_token()
    hash_tok=hash_refresh_token(raw_token)
    family_id=str(uuid.uuid4())
    refresh_token=RefreshToken(
        user_id=user_id,
        token_hash=hash_tok,
        family_id=family_id,
        expires_at=datetime.utcnow()+timedelta(days=7)
    )
    db.add(refresh_token)
    db.commit()
    db.refresh(refresh_token)
    return raw_token 