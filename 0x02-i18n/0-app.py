"""
    0-app.py: a basic flask application

"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
        render an index template
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
