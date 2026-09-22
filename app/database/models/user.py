from ..database import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy.sql import func
from sqlalchemy import String,ForeignKey,DateTime,Text
from datetime import datetime

class User(Base):
    __tablename__="users"

    id: Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(String(50))
    email:Mapped[str]=mapped_column(String(100),unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())
    profile: Mapped["UserProfile"] = relationship(back_populates="user",uselist=False)
    goals: Mapped[list["Goal"]] = relationship(back_populates="user")
    tasks: Mapped[list["Task"]] = relationship(back_populates="user")

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),unique=True)
    plan_description: Mapped[str | None] = mapped_column(Text)
    user: Mapped["User"] = relationship(back_populates="profile")