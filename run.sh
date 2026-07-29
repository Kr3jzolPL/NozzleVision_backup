#!/bin/bash

set -e

cd ~/NozzleVision

source venv/bin/activate

python3 main.py

#!/bin/bash

cd /home/pi/NozzleVision
source .venv/bin/activate

python -m nozzlevision.server