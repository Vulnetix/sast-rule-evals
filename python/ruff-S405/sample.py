# Sample for Ruff rule S405: suspicious-xml-etree-import
# This file is designed to trigger the S405 rule.
# Run: ruff check --select S405 <this_file>

import xml.etree.cElementTree
