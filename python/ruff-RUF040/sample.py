# Sample for Ruff rule RUF040: invalid-assert-message-literal-argument
# This file is designed to trigger the RUF040 rule.
# Run: ruff check --select RUF040 <this_file>

fruits = ["apples", "plums", "pears"]
fruits.filter(lambda fruit: fruit.startwith("p"))
assert len(fruits), 2  # True unless the list is empty
