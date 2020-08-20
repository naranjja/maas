from flask import Flask, request, jsonify
from model import score

app = Flask(__name__)

@app.route("/", methods=["POST"])
def predict():
    x = request.get_json()["x"]
    return jsonify({
        "probabilities": score([x])
    })

app.run()