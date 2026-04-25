# Sample for Ruff rule PLR0202: no-classmethod-decorator
# This file is designed to trigger the PLR0202 rule.
# Run: ruff check --select PLR0202 <this_file>

class Foo:
    def bar(cls): ...

    bar = classmethod(bar)
