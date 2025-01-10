from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv

import smtplib
import os


load_dotenv(find_dotenv(), override=True)


def send_email(data):
    email: EmailMessage = EmailMessage()

    try:
        email["from"] = "Web Portfolio"
        email["to"] = os.environ["TO_EMAIL"]
        email["subject"] = data["subject"]

        msg: str = f'{data["message"]}\n\n\n-CONTACT INFO-\nName: {data["name"]}\nEmail: {data["email"]}'

        email.set_content(msg)

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(os.environ["FROM_EMAIL"], os.environ["PASSWORD"])
            smtp.send_message(email)
            smtp.close()

    except Exception as err:
        print(f"An error occured: {err}")
