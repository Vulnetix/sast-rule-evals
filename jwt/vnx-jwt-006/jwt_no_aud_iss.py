# vnx-jwt-006 eval target
import jwt
import os

SECRET = os.environ.get("JWT_SECRET", "fallback-secret")

# TRIGGERS: jwt.decode() without audience or issuer verification
def verify_token_incomplete(token):
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
    return payload

# TRIGGERS: jwt.decode() with only algorithms specified, no aud/iss
def get_user_from_token(token):
    data = jwt.decode(
        token,
        SECRET,
        algorithms=["HS256"],
        # Missing: audience="my-service", issuer="auth.example.com"
    )
    return data["sub"]

# Safe alternative: always verify audience and issuer
# payload = jwt.decode(
#     token,
#     SECRET,
#     algorithms=["HS256"],
#     audience="my-api-service",
#     issuer="https://auth.example.com",
# )
