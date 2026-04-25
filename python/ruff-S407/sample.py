# Sample for Ruff rule S407: suspicious-xml-expat-import
# This file is designed to trigger the S407 rule.
# Run: ruff check --select S407 <this_file>

import xml.dom.expatbuilder
