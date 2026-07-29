import cv2

CAMERA_URL = "http://192.168.1.117:8080/?action=snapshot"


def capture():

    frame = cv2.imread(CAMERA_URL)

    if frame is not None:
        return frame

    cap = cv2.VideoCapture(CAMERA_URL)

    ok, frame = cap.read()

    cap.release()

    if not ok:
        return None

    return frame