"""
Agent Orchestrator Module
Translates high-level task goals into structured, executable API payloads.
"""

from typing import Dict, Any

class TaskOrchestrator:
    def __init__(self, schema_mapper):
        self.schema_mapper = schema_mapper

    def compose_payload(self, task_goal: str, local_context: Dict[str, Any]) -> Dict[str, Any]:
        endpoint = self.schema_mapper.map_intent_to_endpoint(task_goal)
        payload = {
            "endpoint": endpoint,
            "data": {
                "action": task_goal,
                "sanitized_inputs": local_context.get("public_params", {})
            }
        }
        return payload
