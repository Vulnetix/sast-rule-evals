# Sample for Ruff rule PLC2801: unnecessary-dunder-call
# This file is designed to trigger the PLC2801 rule.
# Run: ruff check --select PLC2801 <this_file>

class C: pass
   c = C()
   c.__gt__(1)  # before fix: NotImplemented
   c > 1        # after fix: raises TypeError
