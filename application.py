from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/shibu")
def shibu():
    return "Hello, shibu!"

@app.route("/arun")
def arun():
    return "Hello, arun!"
