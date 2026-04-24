from flask import Flask
from .database import init_database
from .enviroment import enviroment

def create_app() -> Flask:
    app = Flask(__name__)
    init_database(app, enviroment.database_url)

    @app.get("/health")
    def health():
        return {"status": "ok", "env": enviroment.env}

    return app


app = create_app()
