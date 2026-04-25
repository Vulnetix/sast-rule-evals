# Sample for Ruff rule EM103: dot-format-in-exception
# This file is designed to trigger the EM103 rule.
# Run: ruff check --select EM103 <this_file>

sub = "Some value"
raise RuntimeError("'{}' is incorrect".format(sub))
