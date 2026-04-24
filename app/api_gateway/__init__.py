from flask import Flask

from .health.controller import health_blueprint


def register_controllers(app: Flask) -> None:
    app.register_blueprint(health_blueprint)
