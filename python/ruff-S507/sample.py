# Sample for Ruff rule S507: ssh-no-host-key-verification
# This file is designed to trigger the S507 rule.
# Run: ruff check --select S507 <this_file>

from paramiko import client

ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
