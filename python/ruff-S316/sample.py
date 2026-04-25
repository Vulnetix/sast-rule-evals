# Sample for Ruff rule S316: suspicious-xml-expat-builder-usage
# This file is designed to trigger the S316 rule.
# Run: ruff check --select S316 <this_file>

from xml.dom.expatbuilder import parse

parse("untrusted.xml")
