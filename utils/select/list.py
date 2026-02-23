from InquirerPy import inquirer



def prompt_for_choice(choices):
    return inquirer.fuzzy(
        message="Select an option",
        choices=choices,
        match_exact=False,
        instruction="Type to filter",
    ).execute()
