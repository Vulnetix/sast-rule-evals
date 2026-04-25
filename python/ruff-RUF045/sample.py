# Sample for Ruff rule RUF045: implicit-class-var-in-dataclass
# This file is designed to trigger the RUF045 rule.
# Run: ruff check --select RUF045 <this_file>

@dataclass
class C:
    a = 1
    b: str = ""

C(a = 42)  # TypeError: C.__init__() got an unexpected keyword argument 'a'
