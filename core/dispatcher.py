"""
Task Dispatcher Module
Handles horizontal task queuing, batch splitting, and dynamic node allocation.
"""

import time
import uuid
from typing import List, Dict, Any

class TaskDispatcher:
    def __init__(self):
        self.queue: List[Dict[str, Any]] = []
        self.active_nodes: Dict[str, Dict[str, Any]] = {}

    def register_node(self, node_id: str, capacity: int = 10):
        self.active_nodes[node_id] = {
            "capacity": capacity,
            "active_tasks": 0,
            "last_seen": time.time()
        }
        return {"status": "registered", "node_id": node_id}

    def submit_job_batch(self, job_name: str, tasks: List[Dict[str, Any]]) -> str:
        batch_id = str(uuid.uuid4())
        for task in tasks:
            self.queue.append({
                "batch_id": batch_id,
                "job_name": job_name,
                "task_id": str(uuid.uuid4()),
                "payload": task,
                "status": "pending"
            })
        return batch_id

    def dispatch_next(self, node_id: str) -> Dict[str, Any]:
        if node_id not in self.active_nodes:
            raise ValueError("Node not registered")
        
        for task in self.queue:
            if task["status"] == "pending":
                task["status"] = "assigned"
                task["assigned_to"] = node_id
                self.active_nodes[node_id]["active_tasks"] += 1
                return task
        return {"status": "empty"}
