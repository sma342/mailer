# Email Templates Skill

## Cel umiejętności
Wspieranie tworzenia i testowania szablonów email w projekcie Mailer.
Skill ma pomóc w definiowaniu HTML/Plain text templates, mechanizmów dziedziczenia, podstawowej substytucji zmiennych oraz testów dla wysyłanych wiadomości.

## Kontekst
- Projekt: Mailer
- Nowa funkcjonalność: Email Templates
- Obsługa: HTML i tekst zwykły
- Testowanie: funkcjonalne oraz regresyjne

## Funkcje
- Template inheritance: bazowy layout z sekcjami, które można nadpisywać
- Variable substitution: dynamiczne dane w treści emaila
- HTML/Plain text templates: osobne wersje do renderowania
- Template testing: weryfikacja generowanego outputu i źródła

## Zalecenia
1. Użyj prostego systemu szablonów opartego na Jinja lub podobnej składni
2. Zadbaj o separację warstwy prezentacji od logiki danych
3. Przygotuj fallback dla brakujących pól
4. Zapewnij testy dla różnych scenariuszy wiadomości

## Wzorzec: Bazowy szablon

```jinja
{% raw %}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}Mailer{% endblock %}</title>
</head>
<body>
  <header>{% block header %}Hello from Mailer{% endblock %}</header>
  <main>{% block content %}{% endblock %}</main>
  <footer>{% block footer %}Powered by Mailer{% endblock %}</footer>
</body>
</html>
{% endraw %}
```

## Wzorzec: Szablon wiadomości

```jinja
{% raw %}
{% extends "base_email.html" %}

{% block title %}Welcome, {{ user_name }}!{% endblock %}

{% block content %}
<p>Witaj {{ user_name }},</p>
<p>Dziękujemy za zapisanie się do naszego newslettera.</p>
<p>Twoje konto: {{ user_email }}</p>
{% endblock %}
{% endraw %}
```

## Testowanie
- Sprawdź renderowanie HTML i plaintext
- Weryfikuj obecność wszystkich zmiennych
- Testuj fallbacki dla brakujących danych
- Porównuj wygenerowany output z oczekiwanym

## Przykłady wiadomości
### Welcome
Wiadomość powitalna z imieniem użytkownika i potwierdzeniem adresu email.

### Confirmation
Wiadomość z kodem weryfikacyjnym i linkiem potwierdzającym.

### Newsletter
Szablon z nagłówkiem, sekcją aktualności i stopką marki.

## Wskazówki
- Utrzymuj szablony czytelne i modularne
- Oddziel styl CSS od treści wiadomości
- Używaj prostych placeholderów `{{ name }}` i `{{ url }}`
- Testuj zarówno HTML, jak i plaintext dla każdego szablonu

## Przykład użycia
1. Przygotuj dane kontekstowe
2. Wczytaj szablon HTML i tekstowy
3. Renderuj z kontekstem
4. Wyślij wiadomość przy użyciu `EmailSender`

## Rezultat
Dzięki temu skillowi Copilot powinien pomagać w projektowaniu bezpiecznych i testowalnych szablonów email dla projektu Mailer.
