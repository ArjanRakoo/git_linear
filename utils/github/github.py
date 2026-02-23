import subprocess
import json
import webbrowser
from utils.select import select
class Github:
    def list_review_requests(self):
        requests = self.get_review_requests()

        options = []

        for request in requests:
            options.append({
                "name": request['title'],
                "value": request['url']
            })


        answer = select.prompt_for_choice(options)

        if answer == None:
            return

        webbrowser.open(answer)

    def search(self, type):
        possible_types = ["--review-requested=@me", "--reviewed-by=@me"]

        if type not in possible_types:
            print("Invalid type")
            return

        result = subprocess.run(
            [
                "gh",
                "search",
                "prs",
                type,
                "--state=open",
                "--json",
                "number,title,url",
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("Could not fetch PRs. Is gh installed and authenticated?")
            print(result.stderr.strip())
            return []

        return json.loads(result.stdout or "[]")


    def get_review_requests(self):
        print("Getting review requests...")

        review_requested = self.search("--review-requested=@me")
        reviewed_by = self.search("--reviewed-by=@me")

        options = []

        for pr in review_requested:
            options.append(pr)

        for pr in reviewed_by:
            options.append(pr)

        return options


github = Github()