from app.modules.health.application.health_usecase import HealthUseCase


def test_health_usecase_returns_ok_status_and_env() -> None:
    result = HealthUseCase().execute()

    assert result.status == "ok"
    assert isinstance(result.env, str)
    assert result.env != ""
