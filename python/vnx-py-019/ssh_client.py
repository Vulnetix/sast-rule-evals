# vnx-py-019 eval target
import paramiko

# TRIGGERS: AutoAddPolicy silently trusts any host key
def connect_ssh_bad(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    return client

# TRIGGERS: WarningPolicy logs a warning but still trusts any host key
def connect_ssh_warning(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect(hostname, username=username, password=password)
    return client

# Safe alternative: load known_hosts and use RejectPolicy
# client.load_system_host_keys()
# client.set_missing_host_key_policy(paramiko.RejectPolicy())
