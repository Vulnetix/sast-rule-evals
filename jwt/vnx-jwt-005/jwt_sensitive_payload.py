# vnx-jwt-005 eval target
import jwt
import os

SECRET = os.environ.get("JWT_SECRET", "fallback-secret")

# TRIGGERS: JWT payload contains 'password' key
def create_token_with_password(user_id, username, password):
    payload = {
        "sub": user_id,
        "username": username,
        "password": password,  # DANGER: password in JWT payload
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

# TRIGGERS: jwt.encode() with password in inline dict
def login_token(email, plain_password):
    token = jwt.encode({"email": email, "password": plain_password, "role": "user"}, SECRET)
    return token

# Safe alternative: store only non-sensitive identifiers
# payload = {"sub": user_id, "username": username, "role": "user"}
# token = jwt.encode(payload, SECRET, algorithm="HS256")
