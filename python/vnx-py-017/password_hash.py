# vnx-py-017 eval target
import hashlib

# TRIGGERS: MD5 used to hash a password
def hash_password_bad(password):
    return hashlib.md5(password.encode()).hexdigest()

# TRIGGERS: SHA1 used to hash a password
def hash_password_also_bad(password):
    return hashlib.sha1(password.encode()).hexdigest()

# TRIGGERS: hashlib.new with md5
def hash_with_new(password):
    h = hashlib.new('md5')
    h.update(password.encode())
    return h.hexdigest()

# Safe: use scrypt or bcrypt for passwords
# import bcrypt
# bcrypt.hashpw(password.encode(), bcrypt.gensalt())
