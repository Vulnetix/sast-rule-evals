# Sample for Ruff rule UP005: deprecated-unittest-alias
# This file is designed to trigger the UP005 rule.
# Run: ruff check --select UP005 <this_file>

from unittest import TestCase


class SomeTest(TestCase):
    def test_something(self):
        self.assertEquals(1, 1)
