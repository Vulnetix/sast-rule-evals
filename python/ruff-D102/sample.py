# Sample for Ruff rule D102: undocumented-public-method
# This file is designed to trigger the D102 rule.
# Run: ruff check --select D102 <this_file>

class Cat(Animal):
    def greet(self, happy: bool = True):
        if happy:
            print("Meow!")
        else:
            raise ValueError("Tried to greet an unhappy cat.")
