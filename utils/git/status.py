from pathlib import Path
import subprocess


def print_status():
    cwd = Path.cwd()

    print("--------------------------------")
    subprocess.run(["git", "status"], cwd=cwd)
    print("--------------------------------")