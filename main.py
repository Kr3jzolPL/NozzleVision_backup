import os
import sys
import cv2

from nozzlevision.vision import preprocess
from nozzlevision.detector import detect_blob
from nozzlevision.engine import inspect
import sys

def analyze_live():

    result = inspect()

    if result["status"] == "error":
        print(result["message"])
        sys.exit(2)

    print(result["measurements"])

    if result["status"] == "blob":
        print("STATUS=BLOB")
        sys.exit(1)

    print("STATUS=CLEAN")
    sys.exit(0)


stats = {
    "total": 0,
    "correct": 0,
    "false_positive": 0,
    "false_negative": 0,
}


def analyze(image_path):

    print("=" * 60)
    print(image_path)

    frame = cv2.imread(image_path)

    if frame is None:
        print("Cannot load image")
        return

    pipeline = preprocess(frame)

    measurements = pipeline["measurements"]

    print(measurements)

    detected = detect_blob(measurements)

    folder = os.path.basename(os.path.dirname(image_path)).lower()

    expected_blob = folder != "clean"

    stats["total"] += 1

    if detected == expected_blob:
        stats["correct"] += 1
        result = "✅ CORRECT"

    else:
        result = "❌ WRONG"

        if detected:
            stats["false_positive"] += 1
        else:
            stats["false_negative"] += 1

    print(result)

    if detected:
        print("❌ BLOB DETECTED")
    else:
        print("✅ CLEAN")


def analyze_folder(folder):

    print()
    print("=" * 70)
    print(folder)
    print("=" * 70)

    for filename in sorted(os.listdir(folder)):

        if filename.lower().endswith((".png", ".jpg", ".jpeg")):

            analyze(os.path.join(folder, filename))


def summary():

    print()
    print("=" * 70)
    print("NOZZLEVISION DATASET SUMMARY")
    print("=" * 70)

    print(f"Images checked : {stats['total']}")
    print(f"Correct        : {stats['correct']}")
    print(f"False Positive : {stats['false_positive']}")
    print(f"False Negative : {stats['false_negative']}")

    accuracy = 0

    if stats["total"] > 0:
        accuracy = stats["correct"] / stats["total"] * 100

    print()
    print(f"Accuracy : {accuracy:.2f}%")

    if accuracy >= 98:
        print("🏆 Excellent")

    elif accuracy >= 95:
        print("🟢 Very Good")

    elif accuracy >= 90:
        print("🟡 Good")

    else:
        print("🔴 Needs Improvement")


def main():

    images_root = "images"

    for folder in sorted(os.listdir(images_root)):

        path = os.path.join(images_root, folder)

        if os.path.isdir(path):
            analyze_folder(path)

    summary()


if __name__ == "__main__":
    analyze_live()