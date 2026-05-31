import requests

TOKEN = "你的LINE_TOKEN"

def notify(msg):
    requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {TOKEN}"},
        data={"message": msg}
    )