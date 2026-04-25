# Sample for Ruff rule S310: suspicious-url-open-usage
# This file is designed to trigger the S310 rule.
# Run: ruff check --select S310 <this_file>

from urllib.request import urlopen

url = input("Enter a URL: ")

with urlopen(url) as response:
    ...
