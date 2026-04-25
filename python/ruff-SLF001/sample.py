# Sample for Ruff rule SLF001: private-member-access
# This file is designed to trigger the SLF001 rule.
# Run: ruff check --select SLF001 <this_file>

class Class:
    def __init__(self):
        self._private_member = "..."


var = Class()
print(var._private_member)
