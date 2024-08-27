#!/usr/bin/env python3
"""8. Display the current time"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime


class Config(object):
    """Configuration settings for languages and timezone."""
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default locale
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.timezoneselector
def get_timezone() -> str:
    """Determine the appropriate timezone for the current request."""
    try:
        # Check if timezone is provided in the query parameters
        if request.args.get("timezone"):
            return pytz.timezone(request.args.get("timezone")).zone
        # Fallback to the user's timezone if available
        if g.user and g.user.get("timezone"):
            return pytz.timezone(g.user["timezone"]).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return "UTC"  # Fallback to UTC if no valid timezone is found


def get_user() -> dict:
    """Retrieve the user based on the 'login_as' query parameter."""
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """Set the current user before processing the request."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Select the best language for the current user or request."""
    # Check if locale is provided in the query parameters
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    # Fallback to the user's locale if available
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    # Fallback to the best match from the request headers
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Render the main page with the current time in the user's timezone."""
    current_time = format_datetime(datetime.utcnow())
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
