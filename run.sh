#!/bin/bash

set -e

cd /home/pi/NozzleVision

source venv/bin/activate

python check_api.py