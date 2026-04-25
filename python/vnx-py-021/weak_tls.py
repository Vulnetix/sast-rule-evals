# vnx-py-021 eval target
import ssl

# TRIGGERS: Deprecated SSL/TLS protocol constants
def create_insecure_context_sslv3():
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    return ctx

def create_insecure_context_tls10():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    return ctx

def create_insecure_context_tls11():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
    return ctx

# Safe alternative:
# ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# ctx.minimum_version = ssl.TLSVersion.TLSv1_2
