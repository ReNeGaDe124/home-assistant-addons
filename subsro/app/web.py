from flask import Flask, jsonify
from scanner import scan_movies, scan_tv

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "running"}

@app.route("/scan/movies", methods=["POST"])
def scan_movies_route():
    scan_movies()
    return jsonify({"movies": "ok"})

@app.route("/scan/tv", methods=["POST"])
def scan_tv_route():
    scan_tv()
    return jsonify({"tv": "ok"})
