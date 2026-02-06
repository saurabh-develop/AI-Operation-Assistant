from llm.clients import LLMClient
from llm.prompts import PLANNER_SYSTEM_PROMPT, PLANNER_USER_PROMPT
import json
from core.errors import PlannerError, LLMQuotaError

class PlannerAgent:
    def __init__(self):
        self.llm = LLMClient()  


    def create_plan(self, task: str) -> dict:
        if not task or not task.strip():
            raise PlannerError("Task cannot be empty")
        try:
            response = self.llm.chat(
            system_prompt=PLANNER_SYSTEM_PROMPT,
            user_prompt=PLANNER_USER_PROMPT.format(task=task)
        )
            plan = json.loads(response)
        except RuntimeError as e:
            if "quota" in str(e).lower():
                raise LLMQuotaError(str(e))
            raise PlannerError("Planner LLM failed")
        self._validate_plan(plan)
        return plan
    def _validate_plan(self, plan: dict):
        if "steps" not in plan or not isinstance(plan["steps"], list):
            raise ValueError("Plan must contain a list of steps")
        for step in plan["steps"]:
            if not all(k in step for k in ["tool", "action", "params"]):
                raise ValueError("Each step must have tool, action, params")