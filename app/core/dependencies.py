from ..database.database import SessionLocal,engine,Base
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..schemas.token import TokenData
from ..database.models.user import User
import jwt
from ..core.password import verify_password,hash_password,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY,ALGORITHM
from fastapi import Depends,HTTPException,status

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

def authenticate_user(db :Session,username: str, password: str):
    user=get_user(db,username)
    if not user:
        return False
    if not verify_password(password,user.password_hash):
        return False
    return user

def get_current_user(db:Session=Depends(get_db),token:str=Depends(get_db)):
    credentials_excp=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username is None:
            raise credentials_excp
        token_data=TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_excp
    user=get_user(db,username=token_data.username)
    if user is None:
        raise credentials_excp
    return user


    
