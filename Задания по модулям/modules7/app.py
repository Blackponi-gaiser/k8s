import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "unknown")

@app.route("/")
def root():
    return jsonify({"version": APP_VERSION})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)