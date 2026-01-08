from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

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
    app.run(host="127.0.0.1", port=5000)
