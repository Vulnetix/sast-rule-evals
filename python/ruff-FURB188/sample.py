# Sample for Ruff rule FURB188: slice-to-remove-prefix-or-suffix
# This file is designed to trigger the FURB188 rule.
# Run: ruff check --select FURB188 <this_file>

def example(filename: str, text: str):
    filename = filename[:-4] if filename.endswith(".txt") else filename

    if text.startswith("pre"):
        text = text[3:]
