# Sample for Ruff rule PLW2101: useless-with-lock
# This file is designed to trigger the PLW2101 rule.
# Run: ruff check --select PLW2101 <this_file>

import threading
lock = threading.Lock()
with lock:
    pass  # PLW2101: useless lock context

