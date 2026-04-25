# Sample for Ruff rule SLOT000: no-slots-in-str-subclass
# This file is designed to trigger the SLOT000 rule.
# Run: ruff check --select SLOT000 <this_file>

class MyStr(str):  # SLOT000: no __slots__
    def upper_words(self):
        return self.upper()

