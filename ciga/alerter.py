import os
import smtplib
from email.mime.text import MIMEText


def send_alert_email(new_text):
    sender_email = os.environ.get("EMAIL")
    sender_password = os.environ.get("EMAIL_PASSWORD")
    receiver_email = sender_email

    subject = "CIGA - SAIU UMA ATUALIZAÇÃO NO SITE"
    body = f"\n\n{new_text}\n\n https://consorciociga.gov.br/concursos/"

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
