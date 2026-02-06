# backend_ai/agents/executor.py

from tools.weather_tools import WeatherTool
from tools.github_tools import GitHubTool


class ExecutorAgent:
    def __init__(self):
        # Initialize real tools
        self.weather_tool = WeatherTool()
        self.github_tool = GitHubTool()

        # Tool registry
        self.tools = {
            "weather_api": self._weather_api,
            "github_search": self._github_search,
        }

        # LLM → internal tool aliases
        self.tool_aliases = {
            # Weather
            "weather": "weather_api",
            "weatherapi": "weather_api",
            "weather_api": "weather_api",

            # GitHub / Search
            "github": "github_search",
            "githubsearch": "github_search",
            "github_search": "github_search",
            "search": "github_search",
            "lookup": "github_search",
            "find": "github_search",
        }

    def execute(self, plan: dict) -> list:
        results = []

        for step in plan.get("steps", []):
            raw_tool = step.get("tool", "")
            normalized = raw_tool.strip().lower()
            tool_name = self.tool_aliases.get(normalized)

            print("EXECUTING TOOL:", normalized, "→", tool_name)

            if tool_name not in self.tools:
                raise ValueError(
                    f"Tool '{raw_tool}' not supported. "
                    f"Supported tools: {list(self.tools.keys())}"
                )

            params = step.get("params", {})
            output = self.tools[tool_name](params)

            results.append({
                "tool": tool_name,
                "output": output
            })

        return results

    # -------- REAL TOOL WRAPPERS --------

    def _weather_api(self, params: dict) -> dict:
        city = params.get("city")
        if not city:
            raise ValueError("weather_api requires 'city' param")

        return self.weather_tool.get_weather(city)

    def _github_search(self, params: dict) -> list:
        query = params.get("query")
        limit = params.get("limit", 3)

        if not query:
            raise ValueError("github_search requires 'query' param")

        return self.github_tool.search_repos(query=query, limit=limit)
