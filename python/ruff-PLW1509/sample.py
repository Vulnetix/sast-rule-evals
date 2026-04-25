# Sample for Ruff rule PLW1509: subprocess-popen-preexec-fn
# This file is designed to trigger the PLW1509 rule.
# Run: ruff check --select PLW1509 <this_file>

import os, subprocess

subprocess.Popen(foo, preexec_fn=os.setsid)
subprocess.Popen(bar, preexec_fn=os.setpgid(0, 0))
