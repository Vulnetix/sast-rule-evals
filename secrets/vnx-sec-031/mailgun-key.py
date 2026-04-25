# vnx-sec-031 eval target: Mailgun API key hardcoded
import requests

# TRIGGERS rule
mailgun_api_key = "key-1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d"

response = requests.post(
    "https://api.mailgun.net/v3/example.com/messages",
    auth=("api", mailgun_api_key),
    data={"from": "test@example.com", "to": "user@example.com"},
)
