# Sample for Ruff rule F602: multi-value-repeated-key-variable
# This file is designed to trigger the F602 rule.
# Run: ruff check --select F602 <this_file>

foo = {
    bar: 1,
    baz: 2,
    baz: 3,
}
foo[baz]  # 3
