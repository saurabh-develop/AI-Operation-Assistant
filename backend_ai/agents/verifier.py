from llm.clients import LLMClient
import json


class VerifierAgent:
    def __init__(self):
        self.llm = LLMClient()

    def verify_and_format(self, plan: dict, execution_result: list) -> dict:
        """
        Ensures:
        - No missing steps
        - Non-empty results
        - Clean final structured output
        """

        expected_steps = len(plan.get("steps", []))

        if not isinstance(execution_result, list):
            raise ValueError("Execution result must be a list")

        if len(execution_result) != expected_steps:
            raise ValueError("Execution incomplete: step count mismatch")

        for idx, step_result in enumerate(execution_result):
            if not isinstance(step_result, dict):
                raise ValueError(f"Invalid step result at index {idx}")

            if "tool" not in step_result or "output" not in step_result:
                raise ValueError(f"Missing tool/output at step {idx}")

            if step_result["output"] in (None, [], {}):
                raise ValueError(f"Empty result for tool {step_result['tool']}")

        prompt = f"""
You are a Verifier Agent.

Input plan:
{json.dumps(plan, indent=2)}

Execution results (ordered):
{json.dumps(execution_result, indent=2)}

Rules:
- Produce final user-facing JSON
- Group results by tool name
- Remove execution metadata
- Do NOT add explanations
- Output ONLY valid JSON
"""

        response = self.llm.chat(
            system_prompt="You are a strict JSON formatter.",
            user_prompt=prompt
        )

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            raise ValueError("Verifier output is not valid JSON")
