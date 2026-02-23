from controller import Controller
import argparse

controller = Controller()

optionsMap = {
    "Git Status":  controller.print_git_status,
    "Switch Branch":  controller.switch_branch,
    "Delete Branch":  controller.delete_local_branch,
    "Create Branch from Issue": controller.create_branch_from_issue,
    "List Review Requests": controller.list_review_requests,
}


def build_parser():
    parser = argparse.ArgumentParser(description="Linear + Git helper CLI")

    parser.add_argument("--switch-branch", "--swb", action="store_true", help="Switch Branch")
    parser.add_argument("--delete-branch", "--delb", action="store_true", help="Delete Branch")
    parser.add_argument("--create-branch-from-issue", "--crb", action="store_true", help="Create Branch from Issue")
    parser.add_argument("--list-review-requests", "--rr", action="store_true", help="List Review Requests")

    return parser


def get_main_options():
    options = []

    for choice in optionsMap:
        options.append(choice)

    return options


def handle_args():
    args = build_parser().parse_args()

    if args.switch_branch:
        controller.switch_branch()
        return True

    if args.delete_branch:
        controller.delete_local_branch()
        return True

    if args.create_branch_from_issue:
        controller.create_branch_from_issue()
        return True

    if args.list_review_requests:
        controller.list_review_requests()
        return True

    return False


def run():
    if not controller.check_repo():
        return

    should_exit = handle_args()

    if should_exit:
        return

    while True:
        answer = controller.prompt_for_choice(get_main_options())

        if answer == None:
            break

        optionsMap[answer]()


if __name__ == "__main__":
    run()

