# Sample for Ruff rule PLW0211: bad-staticmethod-argument
# This file is designed to trigger the PLW0211 rule.
# Run: ruff check --select PLW0211 <this_file>

class Wolf:
    @staticmethod
    def eat(self):
        pass
