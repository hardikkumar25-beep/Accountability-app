from datetime import date, datetime
from sqlalchemy import Date, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

class Goal(Base):
    __tablename__ = "goals"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)

    title: Mapped[str] = mapped_column(String(200),nullable=False)
    description: Mapped[str | None] = mapped_column(Text,nullable=True)
    target_date: Mapped[date | None] = mapped_column(Date,nullable=True)
    status: Mapped[str] = mapped_column(String(50),default="active")
    created_at: Mapped[datetime] = mapped_column(DateTime,server_default=func.now())
    
    user: Mapped["User"] = relationship(back_populates="goals")
    tasks: Mapped[list["Task"]] = relationship(back_populates="goal")