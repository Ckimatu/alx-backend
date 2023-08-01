#!/usr/bin/env python3

"""
Force locale with URL parameter
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    # Check if the 'locale' parameter is in the request arguments
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        # Check if the requested locale is in the supported locales
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    # Fall back to the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
