"""
Worker Node Daemon
Runs locally on individual twin setups, executing dispatched jobs and returning proof of work.
"""

import time
import hashlib

class WorkerNode:
    def __init__(self, node_id: str):
        self.node_id = node_id

    def execute_task(self, task: dict) -> dict:
        task_id = task.get("task_id", "unknown")
        print(f"[{self.node_id}] Executing task: {task_id}")
        
        time.sleep(0.1)
        proof = hashlib.sha256(f"{task_id}:{self.node_id}".encode()).hexdigest()

        return {
            "task_id": task_id,
            "node_id": self.node_id,
            "status": "COMPLETED",
            "proof_signature": proof
        }
