# Sample for Ruff rule RUF027: missing-f-string-syntax
# This file is designed to trigger the RUF027 rule.
# Run: ruff check --select RUF027 <this_file>

name = "Sarah"
day_of_week = "Tuesday"
print("Hello {name}! It is {day_of_week} today!")
