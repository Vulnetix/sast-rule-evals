from Crypto.Cipher import DES

# VNX-CRYPTO-004: Broken cipher - DES
key = b"eightkey"
cipher = DES.new(key, DES.MODE_CBC)
