"""
Dynamic Schema Mapper Module
Parses ingested documentation to generate runtime HTTP execution definitions.
"""

from typing import Dict, Any, List

class SchemaMapper:
    def __init__(self, raw_docs: str):
        self.raw_docs = raw_docs

    def extract_endpoints(self) -> List[Dict[str, Any]]:
        endpoints = []
        lines = self.raw_docs.split('\n')
        for line in lines:
            if "GET " in line or "POST " in line or "PUT " in line:
                parts = line.strip().split(' ')
                if len(parts) >= 2:
                    endpoints.append({
                        "method": parts[0],
                        "path": parts[1],
                        "headers": {"Content-Type": "application/json"}
                    })
        return endpoints

    def map_intent_to_endpoint(self, intent: str) -> Dict[str, Any]:
        endpoints = self.extract_endpoints()
        for ep in endpoints:
            if ep["method"] == "POST":
                return ep
        return endpoints[0] if endpoints else {}
