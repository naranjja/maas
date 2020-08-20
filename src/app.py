from flask import Flask, request, jsonify
from celery import Celery
from model import score

app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"], backend=app.config["CELERY_RESULT_BACKEND"])

@celery.task()
def score_async(x):
    return score([x])

@app.route("/start", methods=["POST"])
def start():
    x = request.get_json()["x"]
    task = score_async.apply_async(args=[x], expires=3600)
    return jsonify({
        "task_id": task.id,
    })

@app.route("/check/<task_id>")
def check(task_id):
    task = score_async.AsyncResult(task_id)
    return jsonify({
        "state": task.state,
        "probabilities": task.info,
    })

if __name__ == "__main__":
    app.run(debug=True)