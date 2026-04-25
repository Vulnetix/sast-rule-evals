# Sample for Ruff rule UP023: deprecated-c-element-tree
# This file is designed to trigger the UP023 rule.
# Run: ruff check --select UP023 <this_file>

from xml.etree import cElementTree as ET
