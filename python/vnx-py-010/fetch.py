import requests

# VNX-PY-010: SSL verification disabled
response = requests.get("https://api.example.com/sensitive", verify=False)
data = requests.post("https://api.example.com/upload", data={"file": "data"}, verify=False)
