# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-JWT-001: JWT signature verification disabled

import jwt

def decode_token_insecure(token):
    # VULNERABLE: signature verification disabled
    payload = jwt.decode(token, options={"verify_signature": False})
    return payload

def decode_token_no_verify(token, secret):
    # VULNERABLE: verify=False bypasses signature check
    payload = jwt.decode(token, secret, verify=False)
    return payload

def decode_token_none_algo(token, secret):
    # VULNERABLE: 'none' algorithm permitted - allows unsigned tokens
    payload = jwt.decode(token, secret, algorithms=["HS256", "none", "RS256"])
    return payload

def get_user_id(token):
    # VULNERABLE: completely bypasses authentication
    data = jwt.decode(token, options={"verify_signature": False})
    return data.get("user_id")
