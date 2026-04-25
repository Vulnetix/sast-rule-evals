# Sample for Ruff rule PT027: pytest-unittest-raises-assertion
# This file is designed to trigger the PT027 rule.
# Run: ruff check --select PT027 <this_file>

import unittest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        with self.assertRaises(ValueError):
            raise ValueError("foo")
