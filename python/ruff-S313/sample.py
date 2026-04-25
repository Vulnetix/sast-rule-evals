# Sample for Ruff rule S313: suspicious-xmlc-element-tree-usage
# This file is designed to trigger the S313 rule.
# Run: ruff check --select S313 <this_file>

import xml.etree.ElementTree as ET  # S313
tree = ET.parse("file.xml")

