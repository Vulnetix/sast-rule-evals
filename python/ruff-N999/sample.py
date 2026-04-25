# Sample for Ruff rule N999: invalid-module-name
# N999 fires based on the MODULE FILENAME, not file content.
# The rule triggers when a file/module name does not follow Python naming conventions
# (e.g., contains hyphens, starts with a digit, uses CamelCase, etc.).
# Example filenames that trigger N999: 'my-module.py', '1module.py', 'MyModule.py'
# This sample.py documents the rule but cannot trigger it via content.
# To test: rename this file to 'my-module.py' and run:
#   ruff check --select N999 my-module.py
pass
