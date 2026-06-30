import smtplib
from email.mime.text import MIMEText


def send_email(receiver, score, jd_match):

    sender = "YOUR_GMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD" # Please use your Gmail address and an app-specific password

    if sender == "YOUR_GMAIL@gmail.com" or password == "YOUR_APP_PASSWORD":
        print("Please configure your email and password in email_sender.py")
        return

    body = f"""
Hello,

Resume Score : {score}%

JD Match : {jd_match}%

Thank You.
"""

    msg = MIMEText(body)

    msg["Subject"] = "AI Resume Screening Report"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.send_message(msg)

    server.quit()