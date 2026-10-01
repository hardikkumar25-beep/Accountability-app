from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..core.dependencies import get_db, authenticate_user, get_user
from ..core.password import create_access_token,hash_password,create_refresh_tok_record,hash_refresh_token
from ..schemas.user import UserCreate, UserResponse
from ..schemas.token import Token
from ..database.models.user import User
from ..database.models.ref_toek import RefreshToken
from datetime import datetime,timezone
router=APIRouter()

@router.post("/login",response_model=Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=authenticate_user(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password",headers={"WWW-Authenticate": "Bearer"},)
    access_token=create_access_token(data={"sub":str(user.id)})
    refresh_token = create_refresh_tok_record(db,user.id)
    return {"access_token": access_token, "refresh_token":refresh_token, "token_type": "bearer"}

@router.post("/signup",response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user=get_user(db,username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pass=hash_password(user.password)
    db_user=User(username=user.username,email=user.email,password_hash=hashed_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/refresh",response_model=Token)
def refresh_access_token(refresh_token:str,db:Session=Depends(get_db)):
    token_hash=hash_refresh_token(refresh_token)
    stored_token = (db.query(RefreshToken).filter(RefreshToken.token_hash == token_hash).first())
    if not stored_token:
        raise HTTPException(status_code=401,detail="Invalid refresh token")
    if stored_token.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=401,detail="Refresh token expired")
    if stored_token.revoked:
        family_tokens = (db.query(RefreshToken).filter(RefreshToken.family_id == stored_token.family_id).all())
        for token in family_tokens:
            token.revoked = True
        db.commit()
        raise HTTPException(status_code=401,detail="Refresh token reuse detected")
    stored_token.revoked = True
    user = (db.query(User).filter(User.id == stored_token.user_id).first())
    access_token = create_access_token(data={"sub": str(user.id)})
    new_refresh_token = create_refresh_tok_record(db,user.id,stored_token.family_id)
    return {"access_token": access_token,"refresh_token": new_refresh_token,"token_type": "bearer"}

@router.post("/login")
def logout(refresh_token:str,db:Session=Depends(get_db)):
    token_hash=hash_refresh_token(refresh_token)
    stored_token=db.query(RefreshToken).filter(RefreshToken.token_hash==token_hash).first()
    if stored_token:
        stored_token.revoked=True
        db.commit()
    return {"message":"Logged out successfull"}