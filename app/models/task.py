from datetime import datetime
from typing import Optional
from pydantic import Field
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship;
from app.core.database import db
from app.models.base import BaseModel

# Orm Mapped Class
class task(BaseModel):
    __tablename__="task";
    
    id:Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True);

    name:Mapped[str] = mapped_column(sa.String);
    description:Mapped[Optional[str]] = mapped_column(sa.String, nullable=True);
    date:Mapped[datetime] = mapped_column(sa.DateTime);

    user_id:Mapped[int] = mapped_column(sa.ForeignKey("user.id"))

    user_rel: Mapped["user"] = relationship(back_populates="user")

    def __init__(
            self,
            id=None,
            name=None,
            description=None,
            date=None,
            user_id=None
    ):
        self.id=id;
        self.name=name;
        self.description=description;
        self.date=date; 
        self.user_id=user_id