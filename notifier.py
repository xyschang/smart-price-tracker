import requests
import smtplib
from email.mime.text import MIMEText

TOKEN = "你的LINE_TOKEN"

def notify(msg):
    requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {TOKEN}"},
        data={"message": msg}
    )

def send_mail(subject, body):

    msg = MIMEText(body)

    msg["Subject"] = subject

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        EMAIL,
        PASSWORD
    )

    server.send_message(msg)

    server.quit()