import subprocess
import sys


def run(cmd: list[str]):
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)


if __name__ == "__main__":
    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    run(
        [sys.executable, "-m", "pip", "install", "-e", "."]
    )  # if your project has setup.py or pyproject.toml
