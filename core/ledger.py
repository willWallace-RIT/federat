"""
Dividend Ledger Module
Tracks node execution metrics and calculates lump-sum dividend distributions.
"""

import time
from typing import Dict, Any

class DividendLedger:
    def __init__(self):
        self.node_credits: Dict[str, float] = {}
        self.total_pool_balance: float = 0.0

    def deposit_to_pool(self, amount: float):
        self.total_pool_balance += amount

    def record_completion(self, node_id: str, work_units: float = 1.0):
        self.node_credits[node_id] = self.node_credits.get(node_id, 0.0) + work_units

    def calculate_dividends(self) -> Dict[str, float]:
        total_units = sum(self.node_credits.values())
        if total_units == 0:
            return {}
        
        distributions = {}
        for node_id, units in self.node_credits.items():
            share = (units / total_units) * self.total_pool_balance
            distributions[node_id] = round(share, 4)
        return distributions
