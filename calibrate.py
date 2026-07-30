import json

CONFIG = "config.json"
STEP = 5


def load():
    with open(CONFIG, "r") as f:
        return json.load(f)


def save(cfg):
    with open(CONFIG, "w") as f:
        json.dump(cfg, f, indent=4)


cfg = load()
roi = cfg["roi"]

print("==============================")
print(" NozzleVision ROI Calibration")
print("==============================")
print("")
print("W A S D : Move ROI")
print("I K     : Height +/-")
print("J L     : Width +/-")
print("P       : Save")
print("Q       : Quit")
print("")

while True:

    print(
        f"X:{roi['x']}  "
        f"Y:{roi['y']}  "
        f"W:{roi['width']}  "
        f"H:{roi['height']}"
    )

    key = input("> ").strip().lower()

    if key == "w":
        roi["y"] -= STEP

    elif key == "s":
        roi["y"] += STEP

    elif key == "a":
        roi["x"] -= STEP

    elif key == "d":
        roi["x"] += STEP

    elif key == "i":
        roi["height"] += STEP

    elif key == "k":
        roi["height"] = max(10, roi["height"] - STEP)

    elif key == "l":
        roi["width"] += STEP

    elif key == "j":
        roi["width"] = max(10, roi["width"] - STEP)

    elif key == "p":
        save(cfg)
        print("ROI saved.")

    elif key == "q":
        break