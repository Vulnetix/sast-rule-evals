# Sample for Ruff rule PIE810: multiple-starts-ends-with
# This file is designed to trigger the PIE810 rule.
# Run: ruff check --select PIE810 <this_file>

msg = "Hello, world!"
if msg.startswith("Hello") or msg.startswith("Hi"):
    print("Greetings!")
