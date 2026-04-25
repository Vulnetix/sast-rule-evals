# Sample for Ruff rule PLE1142: await-outside-async
# This file is designed to trigger the PLE1142 rule.
# Run: ruff check --select PLE1142 <this_file>

result = await some_coroutine()  # PLE1142: await outside async

