

from flask import Blueprint, request
from app.models.task import task as Task
from app.core.database import db
api = Blueprint("tasks",__name__,url_prefix="/tasks");

@api.post("/")
def create_task():
    data = request.get_json();
    task = Task(description=data["description"],date=data["date"],name=data["name"]);

    db.session.add(task)
    db.session.commit()
    db.session.refresh(task);

    return task;

@api.get("/single/<int:id>")
def get_one_task():