import random
import string

def generate_token(length=32):
    # VNX-PY-005: random for security-sensitive token generation
    chars = string.ascii_letters + string.digits
    token = "".join(random.choice(chars) for _ in range(length))
    return token

def generate_password():
    # VNX-PY-005: random.randint for password
    password = str(random.randint(100000, 999999))
    return password
