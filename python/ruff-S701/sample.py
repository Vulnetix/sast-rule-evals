# Sample for Ruff rule S701: jinja2-autoescape-false
# This file is designed to trigger the S701 rule.
# Run: ruff check --select S701 <this_file>

import jinja2
env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))  # S701: no autoescape

