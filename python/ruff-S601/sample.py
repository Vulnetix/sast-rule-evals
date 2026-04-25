import paramiko
client = paramiko.SSHClient()
client.connect("host")
stdin, stdout, stderr = client.exec_command("ls")
