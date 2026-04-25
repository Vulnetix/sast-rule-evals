# Sample for Ruff rule RUF035: ruff-unsafe-markup-use
# This file is designed to trigger the RUF035 rule.
# Run: ruff check --select RUF035 <this_file>

from markupsafe import Markup

content = "<script>alert('Hello, world!')</script>"
html = Markup(f"<b>{content}</b>")  # XSS
