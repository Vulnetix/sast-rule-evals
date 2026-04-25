# Sample for Ruff rule E301: blank-line-between-methods
# This file is designed to trigger the E301 rule.
# Run: ruff check --select E301 <this_file>

class MyClass(object):
    def func1():
        pass
    def func2():
        pass
