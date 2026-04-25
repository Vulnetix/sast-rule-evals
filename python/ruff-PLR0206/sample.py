# Sample for Ruff rule PLR0206: property-with-parameters
# This file is designed to trigger the PLR0206 rule.
# Run: ruff check --select PLR0206 <this_file>

class Foo:
    @property
    def get_value(self, default=None):  # PLR0206: property with params
        return self._value

