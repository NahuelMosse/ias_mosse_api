from flask import Blueprint
from app.modules.health.application.health_usecase import HealthUseCase

health_blueprint = Blueprint("health", __name__)


@health_blueprint.get("/health")
def health() -> dict[str, str]:
    result = HealthUseCase().execute()
    return {"status": result.status, "env": result.env}
