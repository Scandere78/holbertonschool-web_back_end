#!/usr/bin/env python3
"""Flask app with Babel locale selector."""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Babel languages and defaults."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Select best match language from request headers."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the home page."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
