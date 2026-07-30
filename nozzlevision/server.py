from flask import Flask, Response
from nozzlevision.engine import inspect
from nozzlevision.camera import capture

import json
import cv2

app = Flask(__name__)


@app.route("/check", methods=["GET", "POST"])
def check():
    return inspect()


@app.route("/calibration")
def calibration():

    with open("config.json", "r") as f:
        config = json.load(f)

    roi = config["roi"]

    frame = capture()

    if frame is None:
        return "Camera unavailable", 500

    cv2.rectangle(
        frame,
        (roi["x"], roi["y"]),
        (
            roi["x"] + roi["width"],
            roi["y"] + roi["height"]
        ),
        (0, 255, 0),
        2
    )

    success, buffer = cv2.imencode(".jpg", frame)

    if not success:
        return "Failed to encode image", 500

    return Response(
        buffer.tobytes(),
        mimetype="image/jpeg"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5050,
        debug=False
    )