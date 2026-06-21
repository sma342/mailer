import os
import smtplib
import ssl
from email.message import EmailMessage
from typing import Optional


class EmailSender:
    def __init__(
        self,
        smtp_host: str = "localhost",
        smtp_port: int = 1025,
        smtp_username: Optional[str] = None,
        smtp_password: Optional[str] = None,
        use_tls: bool = True,
    ):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.use_tls = use_tls

    @classmethod
    def from_env(cls) -> "EmailSender":
        return cls(
            smtp_host=os.getenv("SMTP_HOST", "localhost"),
            smtp_port=int(os.getenv("SMTP_PORT", "1025")),
            smtp_username=os.getenv("SMTP_USERNAME"),
            smtp_password=os.getenv("SMTP_PASSWORD"),
            use_tls=os.getenv("SMTP_USE_TLS", "true").lower() in {"1", "true", "yes"},
        )

    def send(
        self,
        to_email: str,
        subject: str,
        html_body: str,
        text_body: str,
        from_email: str = "noreply@mailer.local",
    ) -> dict:
        message = EmailMessage()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content(text_body)
        message.add_alternative(html_body, subtype="html")

        try:
            if self.use_tls:
                context = ssl.create_default_context()
                with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
                    smtp.starttls(context=context)
                    if self.smtp_username and self.smtp_password:
                        smtp.login(self.smtp_username, self.smtp_password)
                    smtp.send_message(message)
            else:
                with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
                    if self.smtp_username and self.smtp_password:
                        smtp.login(self.smtp_username, self.smtp_password)
                    smtp.send_message(message)

            return {"success": True, "error": None}
        except Exception as exc:
            return {"success": False, "error": str(exc)}
