# Sample for Ruff rule B031: reuse-of-groupby-generator
# This file is designed to trigger the B031 rule.
# Run: ruff check --select B031 <this_file>

import itertools

for name, group in itertools.groupby(data):
    for _ in range(5):
        do_something_with_the_group(group)
