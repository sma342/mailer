import re
from typing import Dict, List, Optional


class SubscriberManager:
    EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    def __init__(self) -> None:
        self._subscribers: Dict[str, Dict[str, str]] = {}

    @staticmethod
    def validate_email(email: str) -> bool:
        if not email or not isinstance(email, str):
            return False
        return bool(SubscriberManager.EMAIL_PATTERN.match(email.strip()))

    def add_subscriber(self, email: str, name: str = "") -> bool:
        if not self.validate_email(email):
            raise ValueError("Invalid email address")
        email = email.strip().lower()
        if email in self._subscribers:
            return False
        self._subscribers[email] = {"email": email, "name": name.strip()}
        return True

    def remove_subscriber(self, email: str) -> bool:
        email = email.strip().lower()
        return self._subscribers.pop(email, None) is not None

    def list_subscribers(self) -> List[Dict[str, str]]:
        return list(self._subscribers.values())

    def get_subscriber(self, email: str) -> Optional[Dict[str, str]]:
        return self._subscribers.get(email.strip().lower())
