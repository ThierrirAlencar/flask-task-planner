from app.server import app

app.config["SQL_ALCHEMY_DATABASE_URI"] = 'sqlite:///teste.db'