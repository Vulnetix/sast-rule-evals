# Sample for Ruff rule RUF068: duplicate-entry-in-dunder-all
# This file is designed to trigger the RUF068 rule.
# Run: ruff check --select RUF068 <this_file>

__all__ = [
    "DatabaseConnection",
    "Product",
    "User",
    "DatabaseConnection",  # Duplicate
]
