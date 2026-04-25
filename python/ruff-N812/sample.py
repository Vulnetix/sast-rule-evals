# Sample for Ruff rule N812: lowercase-imported-as-non-lowercase
# This file is designed to trigger the N812 rule.
# Run: ruff check --select N812 <this_file>

from os.path import Join  # N812: wrong import case

