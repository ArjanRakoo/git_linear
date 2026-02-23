import inquirer
import list_issues


def create_branch():
    print("Create branch")


optionsMap = {
    "Create Branch": create_branch,
    "List Issues": list_issues.list_issues
}


def get_options():
    options = []

    for choice in optionsMap:
        options.append(choice)

    options.append("Exit")

    return options


def create_selectable_list(options):
    return [
        inquirer.List(
            "choice",
            message="Select an option",
            choices=options
        )
    ]


def main_menu():
    is_running = True

    while is_running:
        options = get_options()
        selectable_list = create_selectable_list(options)

        answer = inquirer.prompt(selectable_list)["choice"]

        if answer not in options:
            print("Invalid option")
            continue

        if answer == "Exit":
            is_running = False
            break
        else:
            optionsMap[answer]()


if __name__ == "__main__":
    main_menu()

