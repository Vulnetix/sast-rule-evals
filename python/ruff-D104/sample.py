# Sample for Ruff rule D104: undocumented-public-package
# This file is designed to trigger the D104 rule.
# Run: ruff check --select D104 <this_file>

__all__ = ["Player", "Game"]
