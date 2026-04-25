# VNX-SEC-015: JWT algorithm none
import jwt

token = jwt.encode({"user": "admin"}, key="", algorithm="none")
decoded = jwt.decode(token, options={"verify_signature": False}, algorithms=["none"])
