# Sample for Ruff rule S607: start-process-with-partial-path
# This file is designed to trigger the S607 rule.
# Run: ruff check --select S607 <this_file>

import subprocess
subprocess.run("ls", shell=False)  # S607: partial path

