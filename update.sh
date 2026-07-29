#!/bin/bash

set -e

echo "Updating NozzleVision..."

cd ~/NozzleVision

git pull

source venv/bin/activate

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo ""
echo "Update completed."