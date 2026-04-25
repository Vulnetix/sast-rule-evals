# Sample for Ruff rule N999: invalid-module-name
# This package is named 'MyInvalidPackage' (CamelCase), which violates PEP 8.
# Ruff fires N999 when the directory containing __init__.py uses CamelCase.
# Run: ruff check --select N999 MyInvalidPackage/__init__.py
x = 1
