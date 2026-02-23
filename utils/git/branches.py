import subprocess
from pathlib import Path
from utils.select import list

class Branches:
    def __init__(self):
        self.cwd = Path.cwd()

    def get_local_branches(self):
        result = subprocess.run(
            ["git", "for-each-ref", "--format=%(refname:short)", "refs/heads"],
            cwd=self.cwd,
            capture_output=True,
            text=True,
            check=True,
        )

        return [line.strip() for line in result.stdout.splitlines() if line.strip()]

    def switch_branch(self):
        options = self.get_local_branches()

        options.insert(0, "Cancel")

        answer = list.prompt_for_choice(options)

        if answer == "Cancel":
            return

        print("--------------------------------")
        subprocess.run(["git", "checkout", answer], cwd=self.cwd)

        print(f"Switched to branch {answer}")
        print("--------------------------------")

    def create_branch(self, branch_name):


        print("--------------------------------")
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=self.cwd)

        print(f"Branch {branch_name} created")
        print("--------------------------------")

    def delete_local_branch(self):
        options = self.get_local_branches()

        options.insert(0, "Cancel")

        print("--------------------------------")
        answer = list.prompt_for_choice(options, multi=True)
        

        if ("Cancel" in answer):
            print("Was cancelled")
            return

        for branch in answer:
            subprocess.run(["git", "branch", "-D", branch], cwd=self.cwd)
            print(f"Branch {branch} deleted")

        print("Done!")
        print("--------------------------------")

branches = Branches()