# Sample for Ruff rule PIE807: reimplemented-container-builtin
# This file is designed to trigger the PIE807 rule.
# Run: ruff check --select PIE807 <this_file>

from dataclasses import dataclass, field


@dataclass
class Foo:
    bar: list[int] = field(default_factory=lambda: [])
