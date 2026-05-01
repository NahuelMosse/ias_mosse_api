import importlib


def _set_db_env(monkeypatch) -> None:
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_NAME", "ias")
    monkeypatch.setenv("DB_USER", "user")
    monkeypatch.setenv("DB_PASSWORD", "pass")


def test_debug_enables_only_for_known_truthy_values(monkeypatch) -> None:
    _set_db_env(monkeypatch)
    monkeypatch.setenv("DEBUG", "on")

    environment_module = importlib.import_module("app.enviroment")
    importlib.reload(environment_module)

    assert environment_module.enviroment.debug is True


def test_debug_rejects_untrusted_value(monkeypatch) -> None:
    _set_db_env(monkeypatch)
    monkeypatch.setenv("DEBUG", "true;DROP TABLE users")

    environment_module = importlib.import_module("app.enviroment")
    importlib.reload(environment_module)

    assert environment_module.enviroment.debug is False
