from app import create_app
from app.enviroment import enviroment


def test_get_health_returns_200_and_payload() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "env": enviroment.env}
