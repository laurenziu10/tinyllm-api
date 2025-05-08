from flask import Flask, request, jsonify
from model_handler import classify_text

app = Flask(__name__)

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

if __name__ == "__main__":
    # Run-Button in VS Code kompatibel
    app.run(debug=True, host="0.0.0.0", port=5050)
