# Sample for Ruff rule D105: undocumented-magic-method
# This file is designed to trigger the D105 rule.
# Run: ruff check --select D105 <this_file>

class Cat(Animal):
    def __str__(self) -> str:
        return f"Cat: {self.name}"


cat = Cat("Dusty")
print(cat)  # "Cat: Dusty"
