# Sample for Ruff rule PLE0241: duplicate-bases
# This file is designed to trigger the PLE0241 rule.
# Run: ruff check --select PLE0241 <this_file>

class Foo:
    pass


class Bar(Foo, Foo):
    pass
