#!/usr/bin/python3
""" Starts a Flask web application: """
from flask import Flask


app = Flask(__name__)
app.url_map_strict_slashes = False


@app.route('/')
def hello():
    """ return Hello HBNB! at / """
    return "Hello HBNB!"

@app.route('/airbnb-onepage/')
def airnbnb():
    """ return Hello HBNB! at /airnbnb-onepage """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
