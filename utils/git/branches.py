import subprocess
from pathlib import Path
from utils.select import select

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

        answer = select.prompt_for_choice(options)

        if (answer == None):
            print("Operation cancelled")
            return

        subprocess.run(["git", "checkout", answer], cwd=self.cwd)


    def create_branch(self, branch_name):
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=self.cwd)


    def delete_local_branch(self):
        disabled = {"master", "develop"}

        local_branches = self.get_local_branches()

        options = []

        for branch in local_branches:
            if branch not in disabled:
                options.append(branch)

        answer = select.prompt_for_choice(options, multi=True)
        
        if (answer == None):
            print("Was cancelled")
            return

        for branch in answer:
            subprocess.run(["git", "branch", "-D", branch], cwd=self.cwd)
            print(f"Branch {branch} deleted")



branches = Branches()