def api_config(app):
    app.config["SQL_ALCHEMY_DATABASE_URI"] = 'sqlite:///teste.db'