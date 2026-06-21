import smtplib

from mailer.email_sender import EmailSender


def test_from_env(monkeypatch):
    env = {
        "SMTP_HOST": "smtp.example.com",
        "SMTP_PORT": "587",
        "SMTP_USERNAME": "user",
        "SMTP_PASSWORD": "pass",
        "SMTP_USE_TLS": "true",
    }
    monkeypatch.setattr("os.getenv", lambda key, default=None: env.get(key, default))
    sender = EmailSender.from_env()
    assert sender.smtp_host == "smtp.example.com"
    assert sender.smtp_port == 587
    assert sender.smtp_username == "user"
    assert sender.smtp_password == "pass"
    assert sender.use_tls is True


def test_send_success(monkeypatch):
    class DummySMTP:
        def __init__(self, host, port):
            assert host == "localhost"
            assert port == 1025
        def starttls(self, context=None):
            pass
        def login(self, username, password):
            assert username == "user"
            assert password == "pass"
        def send_message(self, message):
            assert message["To"] == "user@example.com"
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setattr(smtplib, "SMTP", DummySMTP)
    sender = EmailSender("localhost", 1025, "user", "pass", use_tls=True)
    result = sender.send(
        to_email="user@example.com",
        subject="Hello",
        html_body="<p>Hello</p>",
        text_body="Hello",
    )
    assert result["success"]
    assert result["error"] is None


def test_send_failure(monkeypatch):
    class FailedSMTP:
        def __init__(self, host, port):
            pass
        def starttls(self, context=None):
            raise RuntimeError("SMTP error")
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setattr(smtplib, "SMTP", FailedSMTP)
    sender = EmailSender("localhost", 1025, use_tls=True)
    result = sender.send(
        to_email="user@example.com",
        subject="Hello",
        html_body="<p>Hello</p>",
        text_body="Hello",
    )
    assert not result["success"]
    assert "SMTP error" in result["error"]
