import json
import cv2
import numpy as np
import requests
from pathlib import Path

# Load configuration
CONFIG = Path(__file__).resolve().parent.parent / "config.json"

with open(CONFIG, "r") as f:
    config = json.load(f)

CAMERA_URL = config["camera_url"]


def capture():
    try:
        response = requests.get(CAMERA_URL, timeout=5)
        response.raise_for_status()

        data = np.frombuffer(response.content, dtype=np.uint8)
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

        return frame

    except Exception as e:
        print(f"Camera error: {e}")
        return None