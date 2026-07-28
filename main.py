import cv2

from nozzlevision.vision import preprocess
from nozzlevision.detector import detect_blob


def analyze(image_path):

    print("=" * 50)
    print(image_path)

    frame = cv2.imread(image_path)

    if frame is None:
        print("Cannot load image")
        return

    pipeline = preprocess(frame)

    print(pipeline["measurements"])

    if detect_blob(pipeline["measurements"]):
        print("❌ BLOB DETECTED")
    else:
        print("✅ CLEAN")


analyze("images/clean/clean1.png")
analyze("images/clean/clean2.png")
analyze("images/ooze/oozze1.png")