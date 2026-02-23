from dotenv import load_dotenv
import requests
import os
from utils.select import list


load_dotenv()


LINEAR_API_URL="https://api.linear.app/graphql"


def print_list():
    query = """
        query($userId: ID!) {
            issues(filter: {
                state: { type: { eq: "started" } }
                assignee: { id: { eq: $userId } }
            }) {
                nodes { id title identifier branchName }
            }
        }
    """

    variables = { "userId": os.getenv("LINEAR_USER_ID") }

    response = requests.post(
        LINEAR_API_URL,
        headers={
            "Authorization": os.getenv("LINEAR_API_KEY")
        },
        json={
            "query": query,
            "variables": variables
        }
    )

    data = response.json()

    list.prompt_for_choice(create_list_of_branch_names(data))

    


def create_list_of_branch_names(data):
    issues = data["data"]["issues"]["nodes"]

    branch_names = []

    for issue in issues:
        branch_names.append(issue["branchName"])

    return branch_names