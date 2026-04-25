# Sample for Ruff rule UP042: replace-str-enum
# This file is designed to trigger the UP042 rule.
# Run: ruff check --select UP042 <this_file>

import enum


class Foo(str, enum.Enum): ...
