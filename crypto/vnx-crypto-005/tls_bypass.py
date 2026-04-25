import requests

# VNX-CRYPTO-005: TLS certificate validation disabled
response = requests.get("https://api.example.com/data", verify=False)
