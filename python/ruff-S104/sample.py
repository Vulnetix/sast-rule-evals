# Sample for Ruff rule S104: hardcoded-bind-all-interfaces
# This file is designed to trigger the S104 rule.
# Run: ruff check --select S104 <this_file>

import socket
s = socket.socket()
s.bind(("0.0.0.0", 8080))  # S104: binding to all interfaces

