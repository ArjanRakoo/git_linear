from InquirerPy import inquirer

def prompt_for_choice(choices, multi=False):
    if multi:
        return prompt_for_multi_choice(choices)

    return prompt_for_single_choice(choices)


def prompt_for_multi_choice(choices):
    return inquirer.checkbox(
        message="Select issues:",
        choices=choices,
        instruction="Type to filter, Space to toggle, Enter to confirm",
    ).execute()

def prompt_for_single_choice(choices):
    return inquirer.fuzzy(
        message="Select an option",
        choices=choices,
        match_exact=False,
        instruction="Type to filter",
    ).execute()