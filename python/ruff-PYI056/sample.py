# Sample for Ruff rule PYI056: unsupported-method-call-on-all
# This file is designed to trigger the PYI056 rule.
# Run: ruff check --select PYI056 <this_file>

__all__ = ["foo"]
__all__ += ["bar"]  # PYI056: use __all__ = [..., ...]

