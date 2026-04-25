# Sample for Ruff rule FAST003: fast-api-unused-path-parameter
# This file is designed to trigger the FAST003 rule.
# Run: ruff check --select FAST003 <this_file>

from fastapi import FastAPI
app = FastAPI()

@app.route("/items")  # FAST003: use @app.get instead
def list_items():
    return []

