import os
from flask import Flask, flash, redirect, render_template, request, url_for

from .email_sender import EmailSender
from .subscribers import SubscriberManager


def create_app(test_config: dict = None) -> Flask:
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecret")
    app.subscriber_manager = SubscriberManager()
    app.email_sender = EmailSender.from_env()

    if test_config:
        app.config.update(test_config)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            email = request.form.get("email", "")
            name = request.form.get("name", "")
            try:
                added = app.subscriber_manager.add_subscriber(email, name)
                if added:
                    flash("Dziękujemy za zapisanie się", "success")
                else:
                    flash("Ten adres email jest już zapisany.", "info")
            except ValueError:
                flash("Podaj poprawny adres email.", "danger")
            return redirect(url_for("index"))

        return render_template("index.html")

    @app.route("/subscribers")
    def subscribers():
        return render_template(
            "subscribers.html",
            subscribers=app.subscriber_manager.list_subscribers(),
        )

    @app.route("/send-welcome", methods=["POST"])
    def send_welcome():
        email = request.form.get("email", "")
        subscriber = app.subscriber_manager.get_subscriber(email)
        if not subscriber:
            flash("Nie znaleziono subskrybenta.", "danger")
            return redirect(url_for("subscribers"))

        confirmation_link = url_for("index", _external=True)
        html_body = render_template(
            "welcome_email.html",
            user_name=subscriber["name"] or subscriber["email"],
            user_email=subscriber["email"],
            signup_date="today",
            confirmation_link=confirmation_link,
        )
        text_body = render_template(
            "welcome_email.txt",
            user_name=subscriber["name"] or subscriber["email"],
            user_email=subscriber["email"],
            signup_date="today",
            confirmation_link=confirmation_link,
        )

        result = app.email_sender.send(
            to_email=subscriber["email"],
            subject="Welcome to Mailer",
            html_body=html_body,
            text_body=text_body,
        )

        if result["success"]:
            flash("Welcome email wysłany poprawnie.", "success")
        else:
            flash(f"Błąd podczas wysyłki: {result['error']}", "danger")

        return redirect(url_for("subscribers"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
