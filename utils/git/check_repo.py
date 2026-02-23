from pathlib import Path
import subprocess


def is_repo():
    cwd = Path.cwd()

    check_repo = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=cwd,
        capture_output=True,
        text=True,
    )

    if check_repo.returncode != 0:
        print(f"Not a git repository: {cwd}")
        return False

    print(f"Git repository: {cwd}")
    return True

    