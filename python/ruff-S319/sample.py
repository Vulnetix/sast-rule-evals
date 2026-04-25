# Sample for Ruff rule S319: suspicious-xml-pull-dom-usage
# This file is designed to trigger the S319 rule.
# Run: ruff check --select S319 <this_file>

from xml.dom.pulldom import parse

content = parse("untrusted.xml")
