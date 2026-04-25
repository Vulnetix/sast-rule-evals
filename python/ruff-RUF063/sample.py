# Sample for Ruff rule RUF063: access-annotations-from-class-dict
# This file is designed to trigger the RUF063 rule.
# Run: ruff check --select RUF063 <this_file>

foo.__dict__.get("__annotations__", {})
# or
foo.__dict__["__annotations__"]
