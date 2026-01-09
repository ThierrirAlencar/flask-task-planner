from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column;
from app.core.database import db

# Orm Mapped Class
class task(db.Model):
    id:Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True);

    name:Mapped[str] = mapped_column(sa.String);
    description:Mapped[Optional[str]] = mapped_column(sa.String, nullable=True);
    date:Mapped[datetime] = mapped_column(sa.DateTime);

    def __init__(
            self,
            id=None,
            name=None,
            description=None,
            date=None
    ):
        self.id=id;
        self.name=name;
        self.description=description;
        self.date=date; 