# Sample for Ruff rule S704: unsafe-markup-use
# This file is designed to trigger the S704 rule.
# Run: ruff check --select S704 <this_file>

from markupsafe import Markup

content = "<script>alert('Hello, world!')</script>"
html = Markup(f"<b>{content}</b>")  # XSS
