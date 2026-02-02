from sqlalchemy import select
from flask import Blueprint, jsonify, request
from app.models.user import user as User
from app.core.database import db



api = Blueprint("users", __name__, url_prefix="/users")

@api.post("/")
def create_user():
    
    data = request.get_json();
    print(data)
    user = User(name=data["name"],email=data["email"],password=data["password"])

    # cria um usuário
    db.session.add(user)
    # adiciona as alterações
    db.session.commit()
    # 
    db.session.refresh(user);

    return jsonify({"id":user.id,"name":user.name})

@api.delete("/delete/<int:id>")
def delete_user(id):
    user = db.session.scalar(select(User).where(User.id == id))
    if not user:
        return jsonify({"error": "user not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"id": id, "deleted": True})

@api.put("/update/<int:id>")
def update_user(id):

    data = request.get_json(); # corpo da requisição

    user = db.session.scalar(select(User).where(User.id==id));
    user.email==data["email"]
    db.session.commit() # envia as mudanças realizadas

@api.get("/single/<int:id>")
def get_user(id):
    user = db.session.scalar(select(User).where(User.id == id))
    if not user:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email})