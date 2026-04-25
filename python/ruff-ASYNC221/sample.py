# Sample for Ruff rule ASYNC221: run-process-in-async-function
# This file is designed to trigger the ASYNC221 rule.
# Run: ruff check --select ASYNC221 <this_file>

import subprocess


async def foo():
    subprocess.run(cmd)
