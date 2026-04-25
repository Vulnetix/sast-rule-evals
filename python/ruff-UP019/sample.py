# Sample for Ruff rule UP019: typing-text-str-alias
# This file is designed to trigger the UP019 rule.
# Run: ruff check --select UP019 <this_file>

from typing import Text

foo: Text = "bar"
