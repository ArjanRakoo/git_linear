from utils.linear import issues
from utils.git import status, check_repo, branches
from utils.select import list
from controller import Controller

controller = Controller()

optionsMap = {
    "Git Status":  status.print_status,
    "Switch Branch":  branches.branches.switch_branch,
    "Delete Branch":  branches.branches.delete_local_branch,
    "Create Branch from Issue": controller.create_branch_from_issue,
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

