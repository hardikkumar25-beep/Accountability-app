from ..database import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy.sql import func
from sqlalchemy import String,ForeignKey,DateTime,Date,Integer,Time
from datetime import datetime,date,time

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    goal_id: Mapped[int | None] = mapped_column(ForeignKey("goals.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(200))
    desc: Mapped[str] = mapped_column(String(500))
    scheduled_date: Mapped[date] = mapped_column(Date,nullable=False)
    scheduled_time: Mapped[time | None] = mapped_column(Time,nullable=True)
    target_duration: Mapped[int | None] = mapped_column(Integer,nullable=True)
    actual_duration: Mapped[int | None] = mapped_column(Integer,nullable=True)
    deadline: Mapped[datetime | None] = mapped_column(DateTime,nullable=True)
    status: Mapped[str] = mapped_column(String(50),default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime,server_default=func.now())
    completed_at: Mapped[datetime | None] = mapped_column(DateTime,nullable=True)
    user: Mapped["User"] = relationship(back_populates="tasks")
    goal: Mapped["Goal | None"] = relationship(back_populates="tasks")
    events: Mapped[list["TaskEvent"]] = relationship(back_populates="task")

class TaskEvent(Base):
    __tablename__ = "task_events"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    event_type: Mapped[str] = mapped_column(String(50))
    timestamp: Mapped[datetime] = mapped_column(DateTime,server_default=func.now())
    task: Mapped["Task"] = relationship(back_populates="events")




