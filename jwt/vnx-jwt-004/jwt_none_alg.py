# vnx-jwt-004 eval target
import jwt

# TRIGGERS: jwt.encode with algorithm='none' produces unsigned tokens
def create_unsigned_token(payload):
    token = jwt.encode(payload, "", algorithm="none")
    return token

# TRIGGERS: jwt decode accepting 'none' as sole algorithm
def decode_unsigned_token(token):
    return jwt.decode(token, options={"verify_signature": False}, algorithms=["none"])

# Safe alternative:
# import secrets
# secret = secrets.token_hex(32)
# token = jwt.encode(payload, secret, algorithm="HS256")
# decoded = jwt.decode(token, secret, algorithms=["HS256"])
