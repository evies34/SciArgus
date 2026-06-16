from __future__ import annotations

import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)


def send_email(
    html: str,
    subject: str,
    sender_email: str,
    app_password: str,
    receiver_email: str,
) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        print(f"SENDER_EMAIL={sender_email!r}")
        print(f"APP_PASSWORD_LENGTH={len(app_password) if app_password else 0}")
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    logger.info("Email sent to %s", receiver_email)
