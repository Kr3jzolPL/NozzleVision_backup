import json
import sys
import termios
import tty

CONFIG = "config.json"
STEP = 5


def load():
    with open(CONFIG, "r") as f:
        return json.load(f)


def save(cfg):
    with open(CONFIG, "w") as f:
        json.dump(cfg, f, indent=4)


def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

    return key.lower()


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
        f"\rX:{roi['x']}  "
        f"Y:{roi['y']}  "
        f"W:{roi['width']}  "
        f"H:{roi['height']}      ",
        end="",
        flush=True,
    )

    key = get_key()

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
        print("\nROI saved.")

    elif key == "q":
        print()
        break

    else:
        continue

    save(cfg)