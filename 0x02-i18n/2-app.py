#!/usr/bin/env python3
"""2. Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration settings for Babel and supported languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Select the best language match based on
       the request's Accept-Language header"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Render the '2-index.html' template for the root URL ("/")"""
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
