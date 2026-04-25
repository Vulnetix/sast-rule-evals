# Sample for Ruff rule T100: debugger
# This file is designed to trigger the T100 rule.
# Run: ruff check --select T100 <this_file>

import pdb  # T100: debugger
pdb.set_trace()
breakpoint()  # T100

