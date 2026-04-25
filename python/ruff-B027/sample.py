# Sample for Ruff rule B027: empty-method-without-abstract-decorator
# This file is designed to trigger the B027 rule.
# Run: ruff check --select B027 <this_file>

from abc import ABC

class Interface(ABC):
    def process(self):  # B027: should have @abstractmethod
        pass

