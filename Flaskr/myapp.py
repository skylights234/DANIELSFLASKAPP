from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/Subscribe")
def subscribe():
    return "<h1> Subscribed </h1>"
