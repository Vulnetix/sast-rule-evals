# Sample for Ruff rule S501: request-with-no-cert-validation
# This file is designed to trigger the S501 rule.
# Run: ruff check --select S501 <this_file>

import requests
r = requests.get("https://api.example.com", verify=False)  # S501

