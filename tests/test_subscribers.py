import pytest

from mailer.subscribers import SubscriberManager


def test_validate_email_success():
    assert SubscriberManager.validate_email("user@example.com")


def test_validate_email_failure():
    assert not SubscriberManager.validate_email("invalid-email")
    assert not SubscriberManager.validate_email("")
    assert not SubscriberManager.validate_email(None)


def test_add_remove_list_subscribers():
    manager = SubscriberManager()
    assert manager.add_subscriber("user@example.com", "User")
    assert not manager.add_subscriber("user@example.com", "User")
    subscribers = manager.list_subscribers()
    assert len(subscribers) == 1
    assert subscribers[0]["email"] == "user@example.com"
    assert subscribers[0]["name"] == "User"
    assert manager.remove_subscriber("user@example.com")
    assert not manager.remove_subscriber("user@example.com")
    assert manager.list_subscribers() == []


def test_get_subscriber():
    manager = SubscriberManager()
    manager.add_subscriber("foo@bar.com", "Foo")
    assert manager.get_subscriber("foo@bar.com")["name"] == "Foo"
    assert manager.get_subscriber("missing@bar.com") is None
