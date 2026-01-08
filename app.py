from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route("/")
def index():
    return "App is running", 200

@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Permissions-Policy"] = "geolocation=()"
    return response


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    # sadece IP adresine izin ver
    if not re.match(r"^[0-9\.]+$", host):
        return "Invalid host", 400

    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
