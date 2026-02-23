from InquirerPy import inquirer

def prompt_for_choice(choices, multi=False):
    if len(choices) == 0:
        print("No options to select from")
        return None

    try:
        if multi:
            return prompt_for_multi_choice(choices)

        return prompt_for_single_choice(choices)

    except KeyboardInterrupt:
        return None


def prompt_for_multi_choice(choices):
    return inquirer.fuzzy(
        message="Select options:",
        choices=choices,
        instruction="Type to filter, Tab to toggle, Enter to confirm",
        multiselect=True,
        match_exact=False,
    ).execute()

def prompt_for_single_choice(choices):
    return inquirer.fuzzy(
        message="Select an option:",
        choices=choices,
        match_exact=False,
        instruction="Type to filter",
    ).execute()