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

    def get_review_requests(self):
        print("Getting review requests...")

        result = subprocess.run(
            [
                "gh",
                "search",
                "prs",
                "--review-requested=@me",
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

        prs = json.loads(result.stdout or "[]")

        return prs


github = Github()