# Sample for Ruff rule ASYNC210: blocking-http-call-in-async-function
# This file is designed to trigger the ASYNC210 rule.
# Run: ruff check --select ASYNC210 <this_file>

import urllib


async def fetch():
    urllib.request.urlopen("https://example.com/foo/bar").read()
