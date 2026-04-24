from app.enviroment import enviroment
from app.modules.health.domain.health_status import HealthStatus


class HealthUseCase:
    def execute(self) -> HealthStatus:
        return HealthStatus(status="ok", env=enviroment.env)
