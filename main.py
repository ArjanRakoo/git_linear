from controller import Controller

controller = Controller()

optionsMap = {
    "Git Status":  controller.print_git_status,
    "Switch Branch":  controller.switch_branch,
    "Delete Branch":  controller.delete_local_branch,
    "Create Branch from Issue": controller.create_branch_from_issue,
    "List Review Requests": controller.list_review_requests,
}


def get_main_options():
    options = []

    for choice in optionsMap:
        options.append(choice)

    return options


def run():
    if not controller.check_repo():
        return

    while True:
        answer = controller.prompt_for_choice(get_main_options())

        if answer == None:
            break

        optionsMap[answer]()


if __name__ == "__main__":
    run()

