from types import SimpleNamespace

from dotenv import dotenv_values

_raw = dotenv_values(".env")
_truthy = {"1", "true", "yes", "on"}

enviroment = SimpleNamespace(
    env=str(_raw.get("ENV", "development")),
    debug=str(_raw.get("DEBUG", "false")).strip().lower() in _truthy,
)
