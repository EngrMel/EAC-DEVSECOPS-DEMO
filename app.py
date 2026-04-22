from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps"

@app.route("/profile")
def profile():
    name = request.args.get("name")
    return f"<h1>Welcome EAC {name}</h1>"