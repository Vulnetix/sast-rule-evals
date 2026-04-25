# Sample for Ruff rule S201: flask-debug-true
# This file is designed to trigger the S201 rule.
# Run: ruff check --select S201 <this_file>

from flask import Flask
app = Flask(__name__)
app.run(debug=True)  # S201: debug mode

