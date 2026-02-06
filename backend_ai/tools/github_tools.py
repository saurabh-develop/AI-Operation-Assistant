import os
import requests
from tools.base_tools import BaseTool


class GitHubTool(BaseTool):
    BASE_URL = "https://api.github.com"


    def search_repos(self, query: str, limit: int = 3):
        headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"
        }


        def call():
            r = requests.get(
                f"{self.BASE_URL}/search/repositories",
                headers=headers,
                params={"q": query, "sort": "stars", "per_page": limit}
                )
            r.raise_for_status()
            data = r.json()["items"]
            return [
                {
                    "name": repo["full_name"],
                    "stars": repo["stargazers_count"],
                    "description": repo["description"],
                }
                for repo in data
            ]
        
        return self.retry(call)