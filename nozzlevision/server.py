from flask import Flask
from nozzlevision.engine import inspect

app = Flask(__name__)


@app.route("/check", methods=["GET", "POST"])
def check():
    return inspect()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5050,
        debug=False
    )