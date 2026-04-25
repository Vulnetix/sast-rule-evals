# Sample for Ruff rule S601: paramiko-call
# This file is designed to trigger the S601 rule.
# Run: ruff check --select S601 <this_file>

import paramiko
ssh = paramiko.SSHClient()
ssh.exec_command("ls")  # S601

