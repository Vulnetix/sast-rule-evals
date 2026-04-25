from dataclasses import dataclass

@dataclass
class Foo:
    x = 1  # RUF045: implicit class variable in dataclass (no type annotation)
