from typing import Optional
from app.core.database import db
from sqlalchemy.orm import Mapped, mapped_column,relationship;
from typing import List;
import sqlalchemy as sa
from app.models.base import BaseModel


class user(BaseModel):
    __tablename__="user"
    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True,autoincrement=True)
    email:Mapped[str] = mapped_column(sa.String, unique=True);
    name:Mapped[str] = mapped_column(sa.String);
    password:Mapped[str]=mapped_column(sa.String);

    tasks:Mapped[List["task"]] = relationship(back_populates="task");

    def __init__(
            self,
            id=None,
            email=None,
            name=None,
            password=None
    ):
        self.email=email;
        self.id = id;
        self.name=name;
        self.password=password;