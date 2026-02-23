from dotenv import load_dotenv
import os
import requests

load_dotenv()


class Linear:
    def __init__(self):
        self.api_url = "https://api.linear.app/graphql"
        self.api_key = os.getenv("LINEAR_API_KEY")
        self.user_id = os.getenv("LINEAR_USER_ID")

    def get_my_id(self):
        return "query { viewer { id } }"

    def query_me(self):
        print("Getting user id...")
        
        response = requests.post(
            self.api_url,
            json={"query": self.get_my_id()},
            headers={"Authorization": self.api_key})

        data = response.json()
        return data["data"]["viewer"]["id"]


linear = Linear()
