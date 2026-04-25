# Sample for Ruff rule S314: suspicious-xml-element-tree-usage
# This file is designed to trigger the S314 rule.
# Run: ruff check --select S314 <this_file>

from xml.etree.ElementTree import parse

tree = parse("untrusted.xml")  # Vulnerable to XML attacks.
