from flask import Blueprint, request, jsonify
from sqlalchemy import select
from app.models.task import Task
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
def get_one_task(id:int):
    task = db.session.scalar(select(Task).where(Task.id==id))

    return {
        "id":task.id,
        "completed":task.completed,
        "date":task.date,
        "description":task.description,
        "name":task.name,
        "user_id":task.user_id
    };

@api.get("/all/<int:user_id>")
def get_many_by_user(user_id:int):
    tasks =  db.session.scalars(select(Task).where(Task.user_id==user_id));
    return jsonify(tasks)

@api.delete("/<int:id>")
def delete(id: int):
    task = db.session.scalar(select(Task).where(Task.id == id))
    if not task:
        return jsonify({"error": "task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"id": id, "deleted": True})

@api.put("/<int:id>")
def update(id: int):
    data = request.get_json() or {}

    task = db.session.scalar(select(Task).where(Task.id == id))
    if not task:
        return jsonify({"error": "task not found"}), 404

    # Partial updates
    if "name" in data:
        task.name = data.get("name")

    if "description" in data:
        task.description = data.get("description")

    if "date" in data:
        date_val = data.get("date")
        try:
            from datetime import datetime
            if isinstance(date_val, str):
                task.date = datetime.fromisoformat(date_val)
            elif isinstance(date_val, (int, float)):
                task.date = datetime.fromtimestamp(float(date_val))
            else:
                task.date = date_val
        except Exception:
            return jsonify({"error": "invalid date format, expected ISO string or unix timestamp"}), 400

    if "completed" in data:
        task.completed = bool(data.get("completed"))

    if "user_id" in data:
        # Validate that the user exists
        from app.models.user import User
        try:
            new_user_id = int(data.get("user_id"))
        except Exception:
            return jsonify({"error": "invalid user_id"}), 400
        user = db.session.scalar(select(User).where(User.id == new_user_id))
        if not user:
            return jsonify({"error": "user not found"}), 404
        task.user_id = user.id

    db.session.commit()
    db.session.refresh(task)

    return jsonify({
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "date": task.date.isoformat() if task.date else None,
        "completed": task.completed,
        "user_id": task.user_id,
    })