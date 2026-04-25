# Sample for Ruff rule PLE0302: unexpected-special-method-signature
# This file is designed to trigger the PLE0302 rule.
# Run: ruff check --select PLE0302 <this_file>

class Sized:
    def __len__(self, extra):  # PLE0302: wrong args
        return 0

