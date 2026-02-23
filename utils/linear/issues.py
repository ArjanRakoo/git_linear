from dotenv import load_dotenv
import requests
import os
from utils.select import select


load_dotenv()

class Issues:
    def __init__(self):
        self.api_url = "https://api.linear.app/graphql"
        self.api_key = os.getenv("LINEAR_API_KEY")

    def print_list(self, userId):
        data = self.get_issues(userId)

        options = self.create_list_of_branch_names(data)

        return select.prompt_for_choice(options)

        

    def get_issues(self, userId):
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

        variables = { "userId": userId }

        print("Getting issues...")

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

        return response.json()


    def create_list_of_branch_names(self, data):
        issues = data["data"]["issues"]["nodes"]

        branch_names = []

        for issue in issues:
            branch_names.append(issue["branchName"])

        return branch_names

issues = Issues()





    

