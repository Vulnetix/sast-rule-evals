# Sample for Ruff rule S702: mako-templates
# This file is designed to trigger the S702 rule.
# Run: ruff check --select S702 <this_file>

from mako.template import Template

Template("hello")
