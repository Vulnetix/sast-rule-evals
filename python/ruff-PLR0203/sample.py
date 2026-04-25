# Sample for Ruff rule PLR0203: no-staticmethod-decorator
# This file is designed to trigger the PLR0203 rule.
# Run: ruff check --select PLR0203 <this_file>

class Foo:
    def bar(arg1, arg2): ...

    bar = staticmethod(bar)
