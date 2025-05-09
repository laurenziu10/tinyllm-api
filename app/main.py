# Flask REST-API für AG News Klassifikation mit OpenAI
from flask import Flask, request, jsonify, send_from_directory
from model_handler import classify_text
import os
from datasets import load_dataset
import random

app = Flask(__name__)

# POST /predict: JSON-Eingabe mit "text", Rückgabe der Vorhersage-Kategorie
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data["text"]
    category = classify_text(text)
    return jsonify({
        "category": category,
        "input": text
    })

# GET /gui: Lade die interaktive GUI (HTML)
@app.route("/gui")
def gui():
    return send_from_directory(os.path.dirname(__file__), "gui.html")

# GET /: Landing Page
@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "index.html")

# GET /random: Liefert einen zufälligen AG News Artikel (Test-Set)
@app.route("/random")
def random_sample():
    dataset = load_dataset("ag_news", split="test")
    sample = random.choice(dataset)
    return jsonify({
        "text": sample["text"],
        "label": sample["label"]
    })

# Lokaler Startpunkt
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
