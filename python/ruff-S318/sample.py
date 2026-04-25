# Sample for Ruff rule S318: suspicious-xml-mini-dom-usage
# This file is designed to trigger the S318 rule.
# Run: ruff check --select S318 <this_file>

from xml.dom.minidom import parse

content = parse("untrusted.xml")
