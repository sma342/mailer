import pytest

from mailer.web import create_app


def test_index_page():
    app = create_app({"TESTING": True})
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Mailer" in response.data


def test_subscribe_and_list(monkeypatch):
    app = create_app({"TESTING": True})
    client = app.test_client()

    response = client.post("/", data={"email": "test@example.com", "name": "Test User"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Dziękujemy za zapisanie się" in response.get_data(as_text=True)

    response = client.get("/subscribers")
    assert response.status_code == 200
    assert "test@example.com" in response.get_data(as_text=True)
    assert "Test User" in response.get_data(as_text=True)


def test_send_welcome(monkeypatch):
    app = create_app({"TESTING": True})
    app.subscriber_manager.add_subscriber("send@example.com", "Send User")

    class DummySender:
        def send(self, to_email, subject, html_body, text_body, from_email=None):
            return {"success": True, "error": None}

    monkeypatch.setattr(app, "email_sender", DummySender())
    client = app.test_client()
    response = client.post("/send-welcome", data={"email": "send@example.com"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Welcome email wysłany poprawnie" in response.get_data(as_text=True)
