# Sample for Ruff rule S315: suspicious-xml-expat-reader-usage
# This file is designed to trigger the S315 rule.
# Run: ruff check --select S315 <this_file>

from xml.sax.expatreader import create_parser

parser = create_parser()
