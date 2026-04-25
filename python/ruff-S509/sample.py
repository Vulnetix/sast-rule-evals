# Sample for Ruff rule S509: snmp-weak-cryptography
# This file is designed to trigger the S509 rule.
# Run: ruff check --select S509 <this_file>

from pysnmp.hlapi import UsmUserData

UsmUserData("user")
