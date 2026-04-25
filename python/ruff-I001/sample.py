# Sample for Ruff rule I001: unsorted-imports
# This file is designed to trigger the I001 rule.
# Run: ruff check --select I001 <this_file>

import sys
import os  # I001: should come before sys
import json

