from flask import Flask, request
from requests import post, get 
import json


app = Flask(__name__)

CALLBACK = "https://localhost:2345/callback"

@app.route("/")
def ind():
    return f"""
    <html>
    <head><title>Alles Quickauth Demo</title></head>
    <body>
    <a href="https://quickauth.alles.cx/?redirect={CALLBACK}">auth!</a>
    </body>
    </html>
    """

@app.route("/callback")
def cb():
    token = request.args.get("token") # GET `token` parameter
    req = post("https://quickauth.alles.cx", json = {"token": token, "redirect": CALLBACK})
    uid = json.loads(req.text)["id"]
    namereq = get(f"https://horizon.alles.cc/users/{uid}")
    name = json.loads(namereq.text)["name"]
    return f"""
    <html>
    <head><title>Alles Quickauth Demo</title></head>
    <body>
    <p>Hello, {name}!</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 2345)
