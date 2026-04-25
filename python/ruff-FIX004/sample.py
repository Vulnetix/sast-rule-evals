# Sample for Ruff rule FIX004: line-contains-hack
# This file is designed to trigger the FIX004 rule.
# Run: ruff check --select FIX004 <this_file>

import os


def running_windows():  # HACK: Use platform module instead.
    try:
        os.mkdir("C:\\Windows\\System32\\")
    except FileExistsError:
        return True
    else:
        os.rmdir("C:\\Windows\\System32\\")
        return False
