#!/usr/bin/env python3
"""Module to infer appropriate time zone"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


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
    return render_template('7-index.html')


@babel.localeselector
def get_locale() -> str:
    """Method to get language to use"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    user_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if user_locale:
        return user_locale

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """Method to get the timezone"""
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            pytz.timezone(timezone)

        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            pytz.timezone(timezone)

    except pytz.exceptions.UnknownTimeZoneError:
        pass

    return timezone


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
