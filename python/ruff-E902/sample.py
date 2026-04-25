# Sample for Ruff rule E902: IOError (TokenError)
# E902 is raised by ruff when it encounters a file that cannot be read
# or has an OS-level IO error. It is not triggered by Python code content.
# This rule fires when ruff itself encounters a filesystem error reading a file
# (e.g., permissions error, encoding error at the OS level).
# This cannot be demonstrated with a normal .py file - it requires a file
# that causes an IOError when opened (e.g., a file with wrong permissions or
# a special device file).
# Stub: this sample documents the rule but cannot trigger it via content.
pass
