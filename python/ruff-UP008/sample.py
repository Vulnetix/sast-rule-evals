# Sample for Ruff rule UP008: super-call-with-parameters
# This file is designed to trigger the UP008 rule.
# Run: ruff check --select UP008 <this_file>

class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()  # UP008: use super()

