# Sample for Ruff rule F822: undefined-export
# This file is designed to trigger the F822 rule.
# Run: ruff check --select F822 <this_file>

from foo import bar


__all__ = ["bar", "baz"]  # undefined name `baz` in `__all__`
