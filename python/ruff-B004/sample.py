# Sample for Ruff rule B004: unreliable-callable-check
# This file is designed to trigger the B004 rule.
# Run: ruff check --select B004 <this_file>

__all__ = ["foo"]
__all__ += ["bar"]  # B004: don't augment __all__

