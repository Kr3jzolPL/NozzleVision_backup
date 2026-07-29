from nozzlevision.camera import capture
from nozzlevision.vision import preprocess
from nozzlevision.detector import detect_blob


def inspect():
    frame = capture()

    if frame is None:
        return {
            "blob": False,
            "error": "Cannot capture image"
        }

    pipeline = preprocess(frame)
    measurements = pipeline["measurements"]

    detected = detect_blob(measurements)

    return {
        "blob": detected
    }