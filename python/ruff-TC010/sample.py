# Sample for Ruff rule TC010: runtime-string-union
# This file is designed to trigger the TC010 rule.
# Run: ruff check --select TC010 <this_file>

var: "Foo" | None


class Foo: ...
