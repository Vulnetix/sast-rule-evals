# Sample for Ruff rule PIE804: unnecessary-dict-kwargs
# This file is designed to trigger the PIE804 rule.
# Run: ruff check --select PIE804 <this_file>

def foo(bar):
    return bar + 1


print(foo(**{"bar": 2}))  # prints 3

# No typing errors, but results in an exception at runtime.
print(foo(**{"bar": 2, "baz": 3}))
