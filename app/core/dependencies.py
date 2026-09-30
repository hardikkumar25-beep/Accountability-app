from ..database.database import SessionLocal,engine,Base
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..database.models.user import User
from fastapi import Depends

Base.metadata.create_all(bind=engine)
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="auth/token")

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db :Session=Depends(get_db),username: str, password: str):
    user=get_user(db,username)
    if not user:
        return False
    
