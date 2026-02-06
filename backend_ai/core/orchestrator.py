from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent


class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.verifier = VerifierAgent()

    def run(self, task: str) -> dict:
        plan = self.planner.create_plan(task)
        execution_result = self.executor.execute(plan)
        final_output = self.verifier.verify_and_format(plan, execution_result)
        return final_output
