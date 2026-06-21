# Mailer

Mailer is a small Flask-based Python app for managing email subscribers and sending email campaigns.

## Project Structure

- `mailer/` – Application logic
  - `email_sender.py` – Email sending utilities
  - `subscribers.py` – Subscriber management
  - `web.py` – Flask web interface
- `templates/` – HTML and plaintext email templates
- `.copilot/` – Copilot skills and configuration
- `.agents/` – Agent definitions and workflows
- `copilot-instructions.md` – Project-wide Copilot guidelines
- `skills-agents.excersize.md` – Exercise instructions for skills and agents

## Getting Started

1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```powershell
   python mailer/web.py
   ```

## Copilot Integration

The repository includes custom Copilot configuration for this project:

- `copilot-instructions.md` – Global coding standards and guidelines
- `.copilot/skills/` – Custom skills for email validation, testing, templates, and commit guidance
- `.agents/` – Agent definitions for documentation generation

## Available Skills

- `email-validation` – Helps validate email addresses and create tests
- `mailer-complete-testing` – Supports end-to-end Mailer testing scenarios
- `email-templates` – Provides guidance for HTML and plaintext email templates
- `commit-automation` – Helps generate conventional commit messages and Git commands

## Agent

- `docs-generator-agent` – Automates documentation generation for the project

## Usage

- Follow `copilot-instructions.md` for coding standards
- Use Copilot skills from `.copilot/skills/` when writing code, tests, or templates
- Use agents for multi-step tasks like documentation generation

## Continuous Integration

- GitHub Actions workflow is configured in `.github/workflows/autotest.yml`
- Runs on `push` and `pull_request` against `main`
- Installs dependencies from `requirements.txt` and runs `python -m pytest -q`

## Notes

- Keep secrets out of the codebase
- Use environment variables for sensitive values
- Maintain tests for new logic

## License

This project does not include a license file by default.
