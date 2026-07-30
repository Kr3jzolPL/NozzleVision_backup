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
print("Q       : Quit")
print("")

while True:

    print(
        f"X:{roi['x']}  "
        f"Y:{roi['y']}  "
        f"W:{roi['width']}  "
        f"H:{roi['height']}"
    )

    key = input("> ").lower()

    changed = False

    if key == "w":
        roi["y"] -= STEP
        changed = True

    elif key == "s":
        roi["y"] += STEP
        changed = True

    elif key == "a":
        roi["x"] -= STEP
        changed = True

    elif key == "d":
        roi["x"] += STEP
        changed = True

    elif key == "i":
        roi["height"] += STEP
        changed = True

    elif key == "k":
        roi["height"] = max(10, roi["height"] - STEP)
        changed = True

    elif key == "l":
        roi["width"] += STEP
        changed = True

    elif key == "j":
        roi["width"] = max(10, roi["width"] - STEP)
        changed = True

    elif key == "q":
        print("Calibration finished.")
        break

    if changed:
        save(cfg)