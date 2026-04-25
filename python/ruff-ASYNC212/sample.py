# Sample for Ruff rule ASYNC212: blocking-http-call-httpx-in-async-function
# This file is designed to trigger the ASYNC212 rule.
# Run: ruff check --select ASYNC212 <this_file>

import httpx


async def fetch():
    client = httpx.Client()
    response = client.get(...)
