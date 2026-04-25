# Sample for Ruff rule E304: blank-line-after-decorator
# This file is designed to trigger the E304 rule.
# Run: ruff check --select E304 <this_file>

class User(object):

    @property

    def name(self):
        pass
