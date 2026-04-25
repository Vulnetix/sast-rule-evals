# Sample for Ruff rule S508: snmp-insecure-version
# This file is designed to trigger the S508 rule.
# Run: ruff check --select S508 <this_file>

from pysnmp.hlapi import CommunityData

CommunityData("public", mpModel=0)
