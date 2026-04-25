# Sample for Ruff rule RUF066: property-without-return
# This file is designed to trigger the RUF066 rule.
# Run: ruff check --select RUF066 <this_file>

class User:
    @property
    def full_name(self):
        f"{self.first_name} {self.last_name}"
