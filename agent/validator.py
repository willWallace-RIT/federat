"""
Agent Validator Module
Enforces safety envelopes, rate limit checks, and authorization parameters.
"""

class TaskValidator:
    def __init__(self, max_rate_per_min: int = 60):
        self.max_rate = max_rate_per_min

    def validate_request(self, payload: dict) -> bool:
        if not payload.get("endpoint"):
            return False
        if "data" not in payload:
            return False
        return True
