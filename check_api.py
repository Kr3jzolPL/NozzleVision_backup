#!/usr/bin/env python3

import requests
import sys

MOONRAKER = "http://127.0.0.1:7125"
NOZZLEVISION = "http://127.0.0.1:5050/check"

try:
    result = requests.get(NOZZLEVISION, timeout=2).json()

    blob = result["blob"]

    value = 1 if blob else 0

    requests.post(
        f"{MOONRAKER}/printer/gcode/script",
        json={
            "script": f"SET_GCODE_VARIABLE MACRO=NOZZLE_AUTO VARIABLE=blob VALUE={value}"
        },
        timeout=2,
    )

    print("BLOB" if blob else "CLEAN")
    sys.exit(0)

except Exception as e:
    print(e)
    sys.exit(1)