# Sample for Ruff rule PLE0605: invalid-all-format
# This file is designed to trigger the PLE0605 rule.
# Run: ruff check --select PLE0605 <this_file>

__all__ = ["foo"]
__all__ += ["bar"]  # PLE0605: += on __all__

