# GitHub Copilot Instructions - Mailer Project

## 1. Python i Zależności
- Python 3.9+
- PEP 8, linting: flake8, black
- Type hints obowiązkowe
- requirements.txt zawsze aktualny

## 2. Struktura kodu
- Moduły: max 500 linii
- Funkcje: max 50 linii
- Klasy: odpowiadają pojedynczej odpowiedzialności

## 3. Testy
- 80% code coverage
- pytest + pytest-cov
- Mock email i bazy danych

## 4. Bezpieczeństwo
- Brak credentials w kodzie
- Environment variables dla secrets
- Input validation dla emaili
- SQL injection prevention

## 5. Git
- Commity: conventional commits
- Branch naming: feature/*, bugfix/*, docs/*
- PRs: opisane, z testami

## 6. Integracja skill
- Używaj `mailer-complete-testing` do tworzenia i utrzymywania testów
- Używaj `email-validation` przy pracy z logiką walidacji adresów email
- Używaj `email-templates` przy projektowaniu szablonów wiadomości email
- Preferuj użycie odpowiedniego skill zamiast ręcznego tworzenia dużych wzorców testowych lub templatingowych