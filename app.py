from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Pipeline Test App"

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return subprocess.getoutput(f"ping -c 1 {host}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#Kullanıcıdan gelen host değeri hiç kontrol edilmeden
#Shell komutunun içine giriyor