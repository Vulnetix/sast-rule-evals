# Sample for Ruff rule PIE790: unnecessary-placeholder
# This file is designed to trigger the PIE790 rule.
# Run: ruff check --select PIE790 <this_file>

def foo():
    pass  # PIE790: unnecessary pass

def bar():
    ...  # PIE790: unnecessary ellipsis

