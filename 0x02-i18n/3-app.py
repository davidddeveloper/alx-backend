"""
    0-app.py: a basic flask application

"""
from flask_babel import Babel
from flask import Flask
from flask import request
from flask import render_template


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.Config["LANGUAGES"])


@app.route("/")
def home():
    """
        render an index template
    """
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run()
