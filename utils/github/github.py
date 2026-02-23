import subprocess
import json

class Github:
    def get_review_requests(self):
        result = subprocess.run(
            [
                "gh",
                "search",
                "prs",
                "--review-requested=@me",
                # "--state=open",
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