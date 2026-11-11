"""
Node Telemetry & Privacy Isolation Module
Ensures local personal data is stripped before reporting job metrics back to the ledger.
"""

class NodeTelemetry:
    @staticmethod
    def sanitize_proof(raw_output: dict) -> dict:
        return {
            "task_id": raw_output.get("task_id"),
            "status": raw_output.get("status"),
            "proof": raw_output.get("proof_signature")
        }
