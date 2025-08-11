#!/usr/bin/env python3
"""Flask app with basic Babel setup."""

from flask import Flask
from flask_babel import Babel


class Config:
    """Configuration class for Flask and Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    return "<h1>Hello world</h1>"


if __name__ == "__main__":
    app.run()
