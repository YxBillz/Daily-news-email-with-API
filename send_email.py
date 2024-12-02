import smtplib, ssl
import os

def send_email(message, subject):
    host = "smtp.gmail.com"
    port = 465

    username = "okayuokay5@gmail.com"
    password = os.getenv("OKAYPASS")

    receiver = "okayuokay5@gmail.com"
    context = ssl.create_default_context()

    # Combine subject and body, ensuring proper encoding
    email_message = f"Subject: {subject}\n\n{message.decode('utf-8')}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # Specify UTF-8 encoding explicitly for the email
        server.sendmail(username, receiver, email_message.encode('utf-8'))
