from utils.linear import issues
from utils.git import branches, status, check_repo
from utils.select import select
from utils.github import github

class Controller:
    # Options
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

    def delete_local_branch(self):
        branches.branches.delete_local_branch()

    def switch_branch(self):
        branches.branches.switch_branch()

    def print_git_status(self):
        status.print_status()

    def list_review_requests(self):
        github.github.list_review_requests()

    # Helper methods
    def check_repo(self):
        return check_repo.is_repo()

    def prompt_for_choice(self, choices):
        return select.prompt_for_choice(choices)


