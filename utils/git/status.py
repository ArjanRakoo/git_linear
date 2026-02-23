from pathlib import Path
import subprocess


def print_status():
    cwd = Path.cwd()

    check_repo = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=cwd,
        capture_output=True,
        text=True,
    )

    if check_repo.returncode != 0:
        print(f"Not a git repository: {cwd}")
        return

    print("--------------------------------")
    subprocess.run(["git", "status"], cwd=cwd)
    print("--------------------------------")