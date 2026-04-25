# Sample for Ruff rule UP013: convert-typed-dict-functional-to-class
# This file is designed to trigger the UP013 rule.
# Run: ruff check --select UP013 <this_file>

from typing import TypedDict

Foo = TypedDict("Foo", {"a": int, "b": str})
