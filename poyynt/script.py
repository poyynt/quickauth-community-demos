from flask import Flask, request, redirect
from requests import post, get
from urllib.parse import quote 
import json


app = Flask(__name__)

CALLBACK = "https://localhost:2345/callback"

@app.route("/")
def ind():
    return f"""
    <html>
    <a href="https://quickauth.alles.cx/?redirect={CALLBACK}">auth!</a>
    </html>
    """

@app.route("/callback")
def cb():
    token = request.args.get("token")
    req = post("https://quickauth.alles.cx", json = {"token": token, "redirect": CALLBACK})
    res = json.loads(req.text)["id"]
    addt = res
    uid = res.strip()
    addt += uid
    namereq = get(f"https://horizon.alles.cc/users/{uid}")
    name = json.loads(namereq.text)["name"]
    return f"""
    <html>
    <body>
    <p>Hello, {name}!</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 2345)
