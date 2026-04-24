from flask import Flask

from .api_gateway import register_controllers
from .database import init_database
from .enviroment import enviroment


def create_app() -> Flask:
    app = Flask(__name__)
    init_database(app, enviroment.database_url)
    register_controllers(app)

    return app


app = create_app()
