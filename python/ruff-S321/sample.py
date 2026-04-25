# Sample for Ruff rule S321: suspicious-ftp-lib-usage
# This file is designed to trigger the S321 rule.
# Run: ruff check --select S321 <this_file>

from ftplib import FTP  # S321: FTP insecure
ftp = FTP("example.com")

