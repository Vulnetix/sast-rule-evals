# Sample for Ruff rule S317: suspicious-xml-sax-usage
# This file is designed to trigger the S317 rule.
# Run: ruff check --select S317 <this_file>

from xml.sax import make_parser

make_parser()
