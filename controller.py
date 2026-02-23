from utils.linear import issues
from utils.git import branches, status, check_repo
from utils.select import list
from utils.github import github
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

    def delete_local_branch(self):
        branches.branches.delete_local_branch()

    def switch_branch(self):
        branches.branches.switch_branch()

    def print_git_status(self):
        status.print_status()

    def check_repo(self):
        return check_repo.is_repo()

    def prompt_for_choice(self, choices):
        return list.prompt_for_choice(choices)

    def list_review_requests(self):
        requests = github.github.get_review_requests()

        options = []

        for request in requests:
            options.append(f"{request['number']} - {request['title']}")

        answer = list.prompt_for_choice(options)

        if answer == None:
            print("Operation cancelled")
            return

        print(answer)


