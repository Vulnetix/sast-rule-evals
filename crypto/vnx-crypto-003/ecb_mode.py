from Crypto.Cipher import AES

# VNX-CRYPTO-003: AES in ECB mode
key = b"sixteen byte key"
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(b"plaintext block!")
