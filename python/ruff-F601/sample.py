# Sample for Ruff rule F601: multi-value-repeated-key-literal
# This file is designed to trigger the F601 rule.
# Run: ruff check --select F601 <this_file>

foo = {
    "bar": 1,
    "baz": 2,
    "baz": 3,
}
foo["baz"]  # 3
