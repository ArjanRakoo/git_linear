from dotenv import load_dotenv
import requests
import os
from utils.select import list


load_dotenv()

class Issues:
    def __init__(self):
        self.api_url = "https://api.linear.app/graphql"
        self.api_key = os.getenv("LINEAR_API_KEY")
        self.user_id = os.getenv("LINEAR_USER_ID")

    def print_list(self):
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

        variables = { "userId": self.user_id }

        response = requests.post(
            self.api_url,
            headers={
                "Authorization": self.api_key
            },
            json={
                "query": query,
                "variables": variables
            }
        )

        data = response.json()

        options = self.create_list_of_branch_names(data)

        return list.prompt_for_choice(options)

        

    def get_issues(self):
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
            self.api_url,
            headers={
                "Authorization": os.getenv("LINEAR_API_KEY")
            },
            json={
                "query": query,
                "variables": variables
            }
        )

        data = response.json()

        return self.create_list_of_branch_names(data)

    def create_list_of_branch_names(self, data):
        issues = data["data"]["issues"]["nodes"]

        branch_names = []

        for issue in issues:
            branch_names.append(issue["branchName"])

        return branch_names

issues = Issues()





    

