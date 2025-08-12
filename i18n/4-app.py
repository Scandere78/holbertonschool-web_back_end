from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel()


@babel.localeselector
def get_locale():
    # 1️⃣ Vérifie si un paramètre locale est passé dans l'URL
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # 2️⃣ Sinon, fallback sur la langue préférée du navigateur
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')
