# Sample for Ruff rule PLR6301: no-self-use
# This file is designed to trigger the PLR6301 rule.
# Run: ruff check --select PLR6301 <this_file>

class Person:
    def greeting(self):
        print("Greetings friend!")
