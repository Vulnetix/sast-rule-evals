# Sample for Ruff rule PLW0245: super-without-brackets
# This file is designed to trigger the PLW0245 rule.
# Run: ruff check --select PLW0245 <this_file>

class Animal:
    @staticmethod
    def speak():
        return "This animal says something."


class Dog(Animal):
    @staticmethod
    def speak():
        original_speak = super.speak()  # ERROR: `super.speak()`
        return f"{original_speak} But as a dog, it barks!"
