class AIError(Exception):
    """Base class for all AI system errors"""
    code = "AI_ERROR"
    status_code = 500

    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}


class PlannerError(AIError):
    code = "PLANNER_ERROR"
    status_code = 400


class ExecutorError(AIError):
    code = "EXECUTOR_ERROR"
    status_code = 500


class ToolError(AIError):
    code = "TOOL_ERROR"
    status_code = 500


class VerifierError(AIError):
    code = "VERIFIER_ERROR"
    status_code = 500


class LLMQuotaError(AIError):
    code = "LLM_QUOTA_EXCEEDED"
    status_code = 429


class UserInputError(AIError):
    code = "INVALID_USER_INPUT"
    status_code = 400
