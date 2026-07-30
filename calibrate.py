import json
import cv2

from nozzlevision.camera import capture

with open("config.json", "r") as f:
    config = json.load(f)

roi = config["roi"]

while True:

    frame = capture()

    if frame is None:
        continue

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

    cv2.imshow("NozzleVision Calibration", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()