# Sample for Ruff rule FURB189: subclass-builtin
# This file is designed to trigger the FURB189 rule.
# Run: ruff check --select FURB189 <this_file>

class UppercaseDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)


d = UppercaseDict({"a": 1, "b": 2})  # Bypasses __setitem__
print(d)  # {'a': 1, 'b': 2}
