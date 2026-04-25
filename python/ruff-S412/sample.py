# Sample for Ruff rule S412: suspicious-httpoxy-import
# This file is designed to trigger the S412 rule.
# Run: ruff check --select S412 <this_file>

from wsgiref.handlers import CGIHandler
