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
            return

        subprocess.run(["git", "checkout", answer], cwd=self.cwd)


    def create_branch(self, branch_name):
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=self.cwd)


    def delete_local_branch(self):
        disabled = {"master", "main", "develop"}

        options = []

        for branch in self.get_local_branches():
            if branch not in disabled and branch != self.get_current_branch():
                options.append(branch)

        answer = select.prompt_for_choice(options, multi=True)
        
        if (answer == None):
            return

        for branch in answer:
            subprocess.run(["git", "branch", "-D", branch], cwd=self.cwd)
            print(f"Branch {branch} deleted")

    def get_current_branch(self):
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=self.cwd,
            capture_output=True,
            text=True,
        )

        return result.stdout.strip()



branches = Branches()