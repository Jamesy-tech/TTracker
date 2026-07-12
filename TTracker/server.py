from flask import Flask, request, jsonify, send_from_directory
import json
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "tracker-state.json"

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:filename>")
def files(filename):
    return send_from_directory(BASE_DIR, filename)

@app.get("/api/state")
def get_state():
    if DATA_FILE.exists():
        return jsonify(json.loads(DATA_FILE.read_text()))
    return jsonify({})

@app.post("/api/state")
def save_state():
    DATA_FILE.write_text(json.dumps(request.json, indent=2))
    return {"success": True}

app.run(host="0.0.0.0", port=8080)