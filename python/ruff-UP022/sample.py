# Sample for Ruff rule UP022: replace-stdout-stderr
# This file is designed to trigger the UP022 rule.
# Run: ruff check --select UP022 <this_file>

import subprocess

subprocess.run(["foo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
