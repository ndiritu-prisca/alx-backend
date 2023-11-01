#!/usr/bin/env python3
"""Module for mocking logging in"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """A class Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def index() -> str:
    """Method to define index route"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """Method to get language to use"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
    """Method to get the user"""
    id = request.args.get('login_as')
    try:
        return users.get(int(id))
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """Method used to stash user"""
    g.user = get_user()


if __name__ == '__main__':
    app.run()
