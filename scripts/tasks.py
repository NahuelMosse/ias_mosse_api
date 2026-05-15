import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP_DIR = ROOT / ".tmp"
VENV_DIR = ROOT / ".venv"
VENV_PYTHON_LINUX = VENV_DIR / "bin" / "python"
VENV_PYTHON_WINDOWS = VENV_DIR / "Scripts" / "python.exe"
VENV_PYTHON = VENV_PYTHON_LINUX if VENV_PYTHON_LINUX.exists() else VENV_PYTHON_WINDOWS
DOCKER_COMPOSE_FILE = ROOT / "docker" / "db" / "docker-compose.yml"
ENV_FILE = ROOT / ".env"


def run(cmd):
    try:
        return subprocess.call(cmd, cwd=ROOT)
    except KeyboardInterrupt:
        print("\nInterrumpido (Ctrl + C).")
        return 130


def help_text():
    print(
        "Comandos: install | dev | prod | test | db-up | db-down | migrate | seed | db-setup | db-restart | help"
    )
    print("Uso: make <comando>  o  python scripts/tasks.py <comando>")


def ensure_venv():
    if VENV_PYTHON.exists():
        return 0
    return run([sys.executable, "-m", "venv", str(VENV_DIR)])


def py():
    return str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable


def docker_compose(*args):
    return run(
        [
            "docker",
            "compose",
            "--env-file",
            str(ENV_FILE),
            "-f",
            str(DOCKER_COMPOSE_FILE),
            *args,
        ]
    )


def migrate():
    print("No hay migraciones configuradas todavia. (placeholder migrate)")
    return 0


def seed():
    print("No hay seeding configurado todavia. (placeholder seed)")
    return 0


def db_setup() -> int:
    if docker_compose("up", "-d", "--wait") != 0:
        return 1
    if migrate() != 0:
        return 1
    return seed()


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "install":
        ensure_venv()
        return run([py(), "-m", "pip", "install", "-r", "requirements-dev.txt"])
    if cmd == "dev":
        return run([py(), "app.py"])
    if cmd == "prod":
        if sys.platform == "win32":
            print("Error: gunicorn no corre en Windows. Usá 'make dev' para desarrollo local.")
            return 1
        port = os.getenv("PORT", "10000")
        return run([py(), "-m", "gunicorn", "-w", "1", "-b", f"0.0.0.0:{port}", "app:app"])
    if cmd == "test":
        TMP_DIR.mkdir(exist_ok=True)
        return run(
            [py(), "-m", "pytest", "-q", "-s", "-p", "no:cacheprovider", "--basetemp", str(TMP_DIR / "pytest"), "tests"]
        )
    if cmd == "migrate":
        return migrate()
    if cmd == "seed":
        return seed()
    if cmd == "db-up":
        return docker_compose("up", "-d", "--wait")
    if cmd == "db-down":
        return docker_compose("down", "-v")
    if cmd == "db-setup":
        return db_setup()
    if cmd == "db-restart":
        if docker_compose("down", "-v") != 0:
            return 1
        return db_setup()
    help_text()
    return 0 if cmd == "help" else 1


if __name__ == "__main__":
    raise SystemExit(main())
