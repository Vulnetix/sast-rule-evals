# Sample for Ruff rule FURB180: meta-class-abc-meta
# This file is designed to trigger the FURB180 rule.
# Run: ruff check --select FURB180 <this_file>

class MyClass(object):  # FURB180: unnecessary (object)
    pass

