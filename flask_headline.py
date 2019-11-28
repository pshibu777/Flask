from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, world!"
    return render_template("hello.html", headline=headline)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    headline = name
    return render_template("hello.html", headline=headline)
