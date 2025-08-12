#!/usr/bin/env python3
""" Basic Flask app with Babel configuration """

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Configuration for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select the best match language."""
    # Si ?locale=xx est fourni et valide, on l'utilise
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Sinon, on détecte via l'en-tête Accept-Language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Stocke la locale choisie dans g.locale pour le template"""
    g.locale = get_locale()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """Affiche la page d'accueil"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
