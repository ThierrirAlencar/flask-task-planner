from flask import Flask
from app.core.database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///teste.db'


def load_database():
    
    # carregas os modelos
    from app.models.task import task
    from app.models.user import user

    # Carregar o banco de dados
    from app.core.database import db

    db.init_app(app=app);
    return db;

def load_api():
    pass;

def create_app():
    load_api();
    load_database();

    with app.app_context():
        db.create_all() # cria todas as tabelas carregadas
    return app;