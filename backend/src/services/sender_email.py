import smtplib
from email.mime.text import MIMEText
from backend.src.configs.email import STRING_CONNECTION, PORT, EMAIL, PASSWORD


def sender_email(to, subject, text):
    server = smtplib.SMTP(STRING_CONNECTION, PORT)

    server.starttls()

    server.login(EMAIL, PASSWORD)

    message = MIMEText(text)
    message["From"] = EMAIL
    message["To"] = to
    message["Subject"] = subject

    server.sendmail(EMAIL, EMAIL, message.as_string())
