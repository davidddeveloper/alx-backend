"""
    0-app.py: a basic flask application

"""
from flask_babel import Babel
from flask import Flask
from flask import render_template


class Config:
    LANGUAGES = ["en", "fr"]
    TIMEZONES = "UTC"

app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home():
    """
        render an index template
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(port=5000)
