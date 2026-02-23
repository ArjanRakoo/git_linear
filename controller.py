from utils.linear import issues
from utils.git import branches

class Controller:
    def create_branch_from_issue(self):
        answer = issues.issues.print_list()

        if answer == None:
            print("Operation cancelled")
            return

        local_branches = branches.branches.get_local_branches()

        if answer in local_branches:
            print("Branch already exists")
            return

        branches.branches.create_branch(answer)