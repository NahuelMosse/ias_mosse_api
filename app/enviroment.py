from os import getenv
from types import SimpleNamespace
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()
TRUTHY_VALUES = {"1", "true", "yes", "on"}


def _required(name: str) -> str:
    value = getenv(name)
    if not value:
        raise RuntimeError(f"{name} is required. Configure it in your .env file.")
    return value


def _optional(name: str, default: str) -> str:
    return str(getenv(name, default))


def _build_database_url() -> str:
    scheme = _optional("DB_SCHEME", "postgresql")
    host = _required("DB_HOST")
    port = _required("DB_PORT")
    name = _required("DB_NAME")
    user = quote_plus(_required("DB_USER"))
    password = quote_plus(_required("DB_PASSWORD"))
    schema = _required("DB_SCHEMA").strip()
    base_url = f"{scheme}://{user}:{password}@{host}:{port}/{name}"
    options = quote_plus(f"-csearch_path={schema}")
    return f"{base_url}?options={options}"


enviroment = SimpleNamespace(
    env=_optional("ENV", "development"),
    debug=_optional("DEBUG", "false").strip().lower() in TRUTHY_VALUES,
    database_url=_build_database_url(),
)
