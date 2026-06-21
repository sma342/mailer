# Commit Automation Skill

## Cel umiejętności
Pomoc w tworzeniu standardowych wiadomości commit oraz przygotowywaniu poleceń Git do zatwierdzenia zmian.

## Kontekst
- Projekt: Mailer
- Styl commitów: conventional commits
- Cel: spójna historia zmian, lepsze code review i łatwiejsze generowanie changeloga

## Co potrafi skill
- Generuje poprawną wiadomość commit według konwencji `type(scope?): subject`
- Sugeruje typy commitów: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Przygotowuje komendy Git do użycia, np. `git add .` i `git commit -m "..."`
- Pomaga wybrać scope w zależności od modułu lub funkcji

## Zasady
- Format: `type(scope?): subject`
- Subject: mała litera, krótki opis, bez kropki końcowej
- Jeżeli zmiana jest łamiąca, dodaj `BREAKING CHANGE:` w treści commita
- Używaj `chore` dla zadań narzędziowych i konfiguracji

## Przykłady

### Nowa funkcja
```text
feat(email): add welcome email template rendering
```

### Poprawka błędu
```text
fix(email): correct missing confirmation link in welcome template
```

### Dokumentacja
```text
docs(commit): add commit guidance skill documentation
```

## Jak używać
W Copilot Chat napisz:
```text
Use the commit-automation skill to generate a conventional commit message for adding a welcome email template.
```

Jeśli chcesz pełny zestaw poleceń Git, poproś też o `commit commands`:
```text
Generate commit commands for staging and committing the changes.
```

## Workflow
1. Podaj krótki opis zmiany i kontekst modułu
2. Skill generuje sugerowaną wiadomość commit
3. Skill przygotowuje polecenia `git add` i `git commit`
4. Możesz dostosować treść przed wykonaniem

## Wymagania jakości
- Commit musi być zwięzły i jednoznaczny
- Scope powinien odnosić się do konkretnego komponentu lub pliku
- Nie używaj ogólnych treści typu `update` bez kontekstu
- Dodaj więcej szczegółów w treści commita, jeżeli zmiana jest wielowymiarowa
