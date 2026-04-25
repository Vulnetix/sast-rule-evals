# Sample for Ruff rule UP006: non-pep585-annotation
# This file is designed to trigger the UP006 rule.
# Run: ruff check --select UP006 <this_file>

from typing import Dict, List

def process(items: List[str]) -> Dict[str, int]:  # UP006
    return {}

