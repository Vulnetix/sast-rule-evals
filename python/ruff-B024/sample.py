# Sample for Ruff rule B024: abstract-base-class-without-abstract-method
# This file is designed to trigger the B024 rule.
# Run: ruff check --select B024 <this_file>

from abc import ABC

class Base(ABC):  # B024: no @abstractmethod
    def method(self):
        pass

