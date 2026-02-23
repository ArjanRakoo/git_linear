from pathlib import Path


def print_git_status():
    current_dir = Path.cwd()

    print(current_dir)