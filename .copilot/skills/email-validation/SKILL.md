# Email Validation Skill

## Cel umiejętności
Wspieranie tworzenia funkcji walidacji adresów email i kompletnych testów w projekcie Mailer.

## Kontekst
- Projekt: Mailer
- Wymaganie: walidacja subskrybentów i poprawna obsługa adresów email
- Standard: RFC 5322 (uproszczona wersja dla typowych adresów)

## Zalecenia
- Waliduj format i podstawowe ograniczenia długości
- Obsługuj przyjazne aliasy `user+tag@example.com`
- Zwracaj `False` dla pustych wartości i typów innych niż `str`
- Nie wysyłaj emaili w trakcie walidacji

## Wzorzec: Walidator Email

```python
import re

class EmailValidator:
    PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def validate(email: str) -> bool:
        """Waliduj format adresu email."""
        if not email or not isinstance(email, str):
            return False
        return bool(re.match(EmailValidator.PATTERN, email.strip()))
```

## Wzorzec: Testy

```python
import pytest
from validators import EmailValidator

class TestEmailValidator:
    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("user+tag@domain.co.uk", True),
        ("invalid@", False),
        ("@domain.com", False),
        ("user", False),
        ("", False),
    ])
    def test_email_validation(self, email, expected):
        assert EmailValidator.validate(email) == expected
```

## Reguły
- Stosuj pattern oparty na uproszczonym RFC 5322
- Waliduj format oraz podstawowe ograniczenia długości
- Rozdziel logikę walidacji od logiki wysyłania
- Testuj edge case'y i wartości nieliniowe
