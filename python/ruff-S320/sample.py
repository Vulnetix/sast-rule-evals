# Sample for Ruff rule S320: suspicious-xmle-tree-usage
# This file is designed to trigger the S320 rule.
# Run: ruff check --select S320 <this_file>

from lxml import etree

content = etree.parse("untrusted.xml")
