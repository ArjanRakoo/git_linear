import inquirer

def show_options(options):
    return [
        inquirer.List(
            "choice",
            message="Select an option",
            choices=options
        )
    ]

def prompt_for_choice(options):
    return inquirer.prompt(show_options(options))["choice"]