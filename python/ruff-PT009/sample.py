# Sample for Ruff rule PT009: pytest-unittest-assertion
# This file is designed to trigger the PT009 rule.
# Run: ruff check --select PT009 <this_file>

import unittest

class MyTest(unittest.TestCase):
    def test_value(self):
        self.assertEqual(1, 1)  # PT009: use assert

