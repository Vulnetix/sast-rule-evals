import subprocess

# VNX-PY-007: subprocess with shell=True
user_input = "ls"
subprocess.call(user_input, shell=True)
subprocess.run(f"echo {user_input}", shell=True)
