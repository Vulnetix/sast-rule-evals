# Sample for Ruff rule E731: lambda-assignment
# This file is designed to trigger the E731 rule.
# Run: ruff check --select E731 <this_file>

double = lambda x: x * 2  # E731: assign lambda

