# Sample for Ruff rule S609: unix-command-wildcard-injection
# This file is designed to trigger the S609 rule.
# Run: ruff check --select S609 <this_file>

import subprocess

subprocess.Popen(["chmod", "777", "*.py"], shell=True)
