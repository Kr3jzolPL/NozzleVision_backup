# NozzleVision

OpenCV-powered nozzle inspection and automatic blob detection for Klipper.

NozzleVision uses a camera to inspect the printer nozzle before printing. If a filament blob is detected, it can automatically trigger a cleaning routine before continuing the print.

---

## Features

- ✅ Automatic nozzle inspection
- ✅ OpenCV-based blob detection
- ✅ Configurable inspection position
- ✅ Live ROI calibration
- ✅ Browser-based calibration preview
- ✅ Automatic ROI saving
- ✅ Automatic brush retry
- 🚧 Moonraker integration
- 🚧 Browser-only calibration interface
- 🚧 Advanced calibration tools

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kr3jzolPL/NozzleVision.git
cd NozzleVision
```

Make the installer executable:

```bash
chmod +x install.sh
```

Run the installer:

```bash
./install.sh
```

The installer will:

- Install Python dependencies
- Create a virtual environment
- Install the NozzleVision service
- Install the Klipper configuration
- Restart the service

---

## Calibration

Open the calibration page in your browser:

```
http://<printer-ip>:5050/calibration
```

Start the calibration tool:

```bash
cd ~/NozzleVision
./venv/bin/python calibrate.py
```

Controls:

```
W A S D  Move ROI
I K      Resize height
J L      Resize width
Q        Quit
```

Changes are saved automatically.

---

## Configuration

All settings are stored inside:

```
config.json
```

Example:

```json
{
    "inspect_x": 68,
    "inspect_y": 343,
    "inspect_z": 18,

    "camera_url": "http://127.0.0.1/webcam/?action=snapshot",

    "roi": {
        "x": 560,
        "y": 120,
        "width": 180,
        "height": 140
    },

    "threshold": 45,
    "min_blob_area": 120,
    "max_blob_area": 5000,
    "max_attempts": 3
}
```

---

## How it Works

1. Move the nozzle to the inspection position.
2. Capture an image from the camera.
3. Crop the configured ROI.
4. Detect filament blobs using OpenCV.
5. If a blob is detected:
   - Run the cleaning routine.
   - Inspect again.
6. Continue printing when the nozzle is clean.

---

## Project Structure

```
NozzleVision/
│
├── nozzlevision/
│   ├── server.py
│   ├── camera.py
│   ├── detector.py
│   ├── engine.py
│   └── vision.py
│
├── calibrate.py
├── config.json
├── install.sh
├── uninstall.sh
├── update.sh
├── run.sh
└── requirements.txt
```

---

## Roadmap

- [x] Blob detection
- [x] Automatic cleaning retry
- [x] Live ROI calibration
- [x] Browser calibration preview
- [ ] Browser-based calibration controls
- [ ] Threshold calibration
- [ ] Blob size calibration
- [ ] Moonraker component
- [ ] Camera controls
- [ ] Multi-camera support

---

## Requirements

- Klipper
- Moonraker
- Python 3.10+
- OpenCV
- NumPy
- Flask

---

## License

GPL-3.0 License

---

## Contributing

Pull requests, suggestions and bug reports are always welcome.

If you encounter an issue, please open a GitHub issue with as much detail as possible.

---

## Project Status

🚧 **Active Development**

NozzleVision is under active development and new features are added regularly. The current focus is improving calibration, blob detection reliability, and tighter integration with Klipper and Moonraker.
