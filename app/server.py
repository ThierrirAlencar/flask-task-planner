from flask import Flask
from app.core.database import db


def load_database(app):
    # carregas os modelos
    from app.models.task import Task
    from app.models.user import User

    # Inicializa a extensão do banco para a app passada
    db.init_app(app)
    return db


def load_api(app):
    from app.routes.user import api as user_blueprint
    from app.routes.tasks import api as task_blueprint
    # registra uma rota
    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)


def create_app(test_config: dict | None = None):
    """Factory to create and configure the Flask application.

    Pass a `test_config` dict to override configuration (useful for tests).
    """
    app = Flask(__name__)

    # valor padrão, pode ser sobrescrito por `test_config`
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///teste.db")

    if test_config:
        app.config.update(test_config)

    with app.app_context():
        load_database(app)
        db.create_all()  # cria todas as tabelas carregadas
        load_api(app)

    return app