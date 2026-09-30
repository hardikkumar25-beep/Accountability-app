from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..core.dependencies import get_db, authenticate_user, get_user
from ..core.password import create_access_token,hash_password
from ..schemas.user import UserCreate, UserResponse
from ..database.models.user import User

router=APIRouter()

@router.post("/login",response_model=Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=authenticate_user(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password",headers={"WWW-Authenticate": "Bearer"},)
    access_token=create_access_token(data={"sub":user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup",response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user=get_user(db,username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pass=hash_password(user.password)
    db_user=User(username=user.username,password_hash=hashed_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user