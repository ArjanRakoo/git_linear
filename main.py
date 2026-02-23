from utils.linear import issues
from utils.git import status, check_repo, branches
from utils.select import list


def create_branch():
    answer = issues.issues.print_list()

    if answer == None:
        print("Operation cancelled")
        return

    local_branches = branches.branches.get_local_branches()

    if answer in local_branches:
        print("Branch already exists")
        return

    branches.branches.create_branch(answer)


optionsMap = {
    "Git Status":  status.print_status,
    "Switch Branch":  branches.branches.switch_branch,
    "Delete Branch":  branches.branches.delete_local_branch,
    "Create Branch from Issue": create_branch,
}


def get_main_options():
    options = []

    for choice in optionsMap:
        options.append(choice)

    return options


def run():
    if not check_repo.is_repo():
        return

    is_running = True

    while is_running:
        options = get_main_options()
        answer = list.prompt_for_choice(options)
        if answer == None:
            print("Operation cancelled")
            is_running = False
            break

        if answer == "Exit":
            is_running = False
            break
        else:
            optionsMap[answer]()


if __name__ == "__main__":
    run()

