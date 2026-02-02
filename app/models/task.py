from datetime import datetime
from typing import Optional
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import BaseModel


class Task(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(sa.String(1024), nullable=True)
    date: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.utcnow, nullable=False)

    user_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="tasks")

    completed: Mapped[bool] = mapped_column(sa.Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"<Task id={self.id} name={self.name} user_id={self.user_id}>"