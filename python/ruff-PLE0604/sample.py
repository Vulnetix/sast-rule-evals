# Sample for Ruff rule PLE0604: invalid-all-object
# This file is designed to trigger the PLE0604 rule.
# Run: ruff check --select PLE0604 <this_file>

__all__ = [Foo, 1, None]
