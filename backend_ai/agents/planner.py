from llm.clients import LLMClient
from llm.prompts import PLANNER_SYSTEM_PROMPT, PLANNER_USER_PROMPT
import json


class PlannerAgent:
    def __init__(self):
        self.llm = LLMClient()  


    def create_plan(self, task: str) -> dict:
        response = self.llm.chat(
            system_prompt=PLANNER_SYSTEM_PROMPT,
            user_prompt=PLANNER_USER_PROMPT.format(task=task)
        )
        try:
            plan = json.loads(response)
        except json.JSONDecodeError:
            raise ValueError("Planner output is not valid JSON")
        self._validate_plan(plan)
        return plan
    def _validate_plan(self, plan: dict):
        if "steps" not in plan or not isinstance(plan["steps"], list):
            raise ValueError("Plan must contain a list of steps")
        for step in plan["steps"]:
            if not all(k in step for k in ["tool", "action", "params"]):
                raise ValueError("Each step must have tool, action, params")