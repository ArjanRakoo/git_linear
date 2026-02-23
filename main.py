import inquirer
from utils.linear import issues
from utils.git import status, check_repo
from utils.select import list    


def create_branch():
    print("Create branch")


optionsMap = {
    "Create Branch": create_branch,
    "List Issues": issues.print_list,
    "Git Status": status.print_status,
}


def get_main_options():
    options = []

    for choice in optionsMap:
        options.append(choice)

    options.append("Exit")

    return options


def run():
    if not check_repo.is_repo():
        return

    is_running = True

    while is_running:
        options = get_main_options()
        answer = list.prompt_for_choice(options)

        if answer not in options:
            print("Invalid option")
            continue

        if answer == "Exit":
            is_running = False
            break
        else:
            optionsMap[answer]()


if __name__ == "__main__":
    run()

