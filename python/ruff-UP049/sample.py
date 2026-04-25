# Sample for Ruff rule UP049: private-type-parameter
# This file is designed to trigger the UP049 rule.
# Run: ruff check --select UP049 <this_file>

class GenericClass[_T]:
    var: _T


def generic_function[_T](var: _T) -> list[_T]:
    return var[0]
