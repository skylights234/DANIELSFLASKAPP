from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return "<h1> home page </h1>"

@app.route("/Subscribe")
def subscribe():
    return "<h1> Subscribed </h1>"
