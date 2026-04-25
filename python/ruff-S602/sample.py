# Sample for Ruff rule S602: subprocess-popen-with-shell-equals-true
# This file is designed to trigger the S602 rule.
# Run: ruff check --select S602 <this_file>

import subprocess
subprocess.run("ls -la", shell=True)  # S602: shell=True

