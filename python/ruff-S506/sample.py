# Sample for Ruff rule S506: unsafe-yaml-load
# This file is designed to trigger the S506 rule.
# Run: ruff check --select S506 <this_file>

import yaml
data = yaml.load(stream)  # S506: unsafe yaml.load

