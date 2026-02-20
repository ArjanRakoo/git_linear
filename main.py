import inquirer
import list_issues

def create_branch():
    print("Create branch")

options = {
    "Create Branch": create_branch,
    "List Issues": list_issues.list_issues
}

def get_options():
    choices = []

    for choice in options:
        choices.append(choice)

    choices.append("Exit")

    questions = [
        inquirer.List(
            "choice",
            message="Select an option",
            choices=choices
        )
    ]

    return questions




def main_menu():
    is_running = True

    while is_running:
        answer = inquirer.prompt(get_options())["choice"]
        if answer == "Exit":
            is_running = False
        if answer == "List Issues":
            list_issues.list_issues()
if __name__ == "__main__":
    main_menu()

