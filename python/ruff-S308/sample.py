# Sample for Ruff rule S308: suspicious-mark-safe-usage
# This file is designed to trigger the S308 rule.
# Run: ruff check --select S308 <this_file>

from django.utils.safestring import mark_safe


def render_username(username):
    return mark_safe(f"<i>{username}</i>")  # Dangerous if username is user-provided.
