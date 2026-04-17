import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP_DIR = ROOT / ".tmp"
VENV_DIR = ROOT / ".venv"
VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"


def run(cmd):
    try:
        return subprocess.call(cmd, cwd=ROOT)
    except KeyboardInterrupt:
        print("\nInterrumpido (Ctrl + C).")
        return 130


def help_text():
    print("Comandos: install | run | test | clean-temp | help")
    print("Uso: make <comando>  o  python scripts/tasks.py <comando>")


def ensure_venv():
    if VENV_PYTHON.exists():
        return 0
    return run([sys.executable, "-m", "venv", str(VENV_DIR)])


def py():
    return str(VENV_PYTHON)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "install":
        ensure_venv()
        return run([py(), "-m", "pip", "install", "-r", "requirements-dev.txt"])
    if cmd == "run":
        return run([py(), "app.py"])
    if cmd == "test":
        TMP_DIR.mkdir(exist_ok=True)
        return run(
            [py(), "-m", "pytest", "-q", "-s", "-p", "no:cacheprovider", "--basetemp", str(TMP_DIR / "pytest"), "tests"]
        )
    help_text()
    return 0 if cmd == "help" else 1


if __name__ == "__main__":
    raise SystemExit(main())
