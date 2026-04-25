# Sample for Ruff rule RUF049: dataclass-enum
# This file is designed to trigger the RUF049 rule.
# Run: ruff check --select RUF049 <this_file>

@dataclass
class E(Enum):
    A = 1
    B = 2

print(E.A == E.B)  # True
