from tools.weather_tools import WeatherTool
from tools.github_tools import GitHubTool
from core.errors import ExecutorError, ToolError

class ExecutorAgent:
    def __init__(self):
        self.weather_tool = WeatherTool()
        self.github_tool = GitHubTool()

        self.tools = {
            "weather_api": self._weather_api,
            "github_search": self._github_search,
        }

        self.tool_aliases = {
            "weather": "weather_api",
            "weatherapi": "weather_api",
            "weather_api": "weather_api",

            "github": "github_search",
            "githubsearch": "github_search",
            "github_search": "github_search",
            "search": "github_search",
            "lookup": "github_search",
            "find": "github_search",
        }

    def execute(self, plan: dict) -> list:
        results = []

        for idx, step in enumerate(plan.get("steps", [])):
            raw_tool = step.get("tool", "")
            normalized = raw_tool.strip().lower()
            tool_name = self.tool_aliases.get(normalized)

            print("EXECUTING TOOL:", normalized, "→", tool_name)

           
            if not tool_name:
                raise ExecutorError(
                    f"Unsupported tool '{raw_tool}'",
                    details={"step": idx}
                )
            try:
                params = step.get("params", {})
                output = self.tools[tool_name](params)
            except Exception as e:
                raise ToolError(
                    f"Tool '{tool_name}' failed",
                    details={"error": str(e), "step": idx}
                )
            results.append({
                "tool": tool_name,
                "output": output
            })

        return results

    def _weather_api(self, params: dict) -> dict:
        city = params.get("city")
        if not city:
            raise ToolError("weather_api requires 'city' parameter")
        try:
            return self.weather_tool.get_weather(city)
        except Exception as e:
            raise ToolError("Weather API request failed", {"city": city})

    def _github_search(self, params: dict) -> list:
        query = params.get("query")
        limit = params.get("limit", 3)

        if not query:
            raise ValueError("github_search requires 'query' param")

        return self.github_tool.search_repos(query=query, limit=limit)
