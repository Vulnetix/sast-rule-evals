# Sample for Ruff rule C419: unnecessary-comprehension-in-call
# This file is designed to trigger the C419 rule.
# Run: ruff check --select C419 <this_file>

any([x.id for x in bar])
all([x.id for x in bar])
sum([x.val for x in bar])
min([x.val for x in bar])
max([x.val for x in bar])
