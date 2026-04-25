# Sample for Ruff rule D106: undocumented-public-nested-class
# This file is designed to trigger the D106 rule.
# Run: ruff check --select D106 <this_file>

class Foo:
    """Class Foo."""

    class Bar: ...


bar = Foo.Bar()
bar.__doc__  # None
