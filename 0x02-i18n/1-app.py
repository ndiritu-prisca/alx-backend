#!/usr/bin/env python3
"""Module for a basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """A class Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def index() -> str:
    """Method to define index route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
