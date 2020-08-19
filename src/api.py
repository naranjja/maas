import flask
from model import score
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/", methods=["POST"])
def predict():
    x = request.get_json()["x"]
    return jsonify({
        "probabilities": score([x])
    })

app.run()