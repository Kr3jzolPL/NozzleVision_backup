#!/bin/bash

set -e

echo "Installing NozzleVision..."

INSTALL_DIR="$HOME/NozzleVision"

if [ ! -d "$INSTALL_DIR" ]; then
    git clone https://github.com/Kr3jzolPL/NozzleVision_backup.git "$INSTALL_DIR"
else
    echo "Repository already exists."
fi

cd "$INSTALL_DIR"

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip setuptools wheel

pip install -r requirements.txt

echo ""
echo "Installation completed."
echo ""
echo "Run with:"
echo "~/NozzleVision/venv/bin/python ~/NozzleVision/main.py"