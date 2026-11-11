"""
Doc Ingester Module
Fetches and sanitizes raw API documentation sources (Markdown, HTML, OpenAPI/Swagger).
"""

import re

class DocIngester:
    def __init__(self, doc_source: str):
        self.doc_source = doc_source

    def fetch_raw_content(self) -> str:
        if self.doc_source.endswith(".md") or "markdown" in self.doc_source:
            return "# Sample API\nGET /api/v1/jobs\nPOST /api/v1/tasks"
        return "{"openapi": "3.0.0", "info": {"title": "Work API"}}"

    def sanitize_text(self, text: str) -> str:
        clean = re.sub(r'<[^>]+>', '', text)
        return ' '.join(clean.split())
