#!/bin/bash

set -e

echo "Installing NozzleVision..."

sudo apt update
sudo apt install -y \
    git \
    python3 \
    python3-pip \
    python3-venv

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

chmod +x install.sh update.sh run.sh uninstall.sh

############################################################
# Install Klipper configuration
############################################################

echo "Installing Klipper configuration..."

cp moonraker/nozzlevision.cfg \
    "$HOME/printer_data/config/nozzlevision.cfg"

PRINTER_CFG="$HOME/printer_data/config/printer.cfg"

if ! grep -qF "[include nozzlevision.cfg]" "$PRINTER_CFG"; then
    if grep -q "^#\*#" "$PRINTER_CFG"; then
        awk '
        !inserted && /^#\*#/ {
            print "[include nozzlevision.cfg]"
            print ""
            inserted=1
        }
        { print }
        ' "$PRINTER_CFG" > "$PRINTER_CFG.tmp"

        mv "$PRINTER_CFG.tmp" "$PRINTER_CFG"

        echo "Inserted [include nozzlevision.cfg] before SAVE_CONFIG block"
    else
        echo "" >> "$PRINTER_CFG"
        echo "[include nozzlevision.cfg]" >> "$PRINTER_CFG"
        echo "Added [include nozzlevision.cfg] to end of printer.cfg"
    fi
else
    echo "printer.cfg already includes nozzlevision.cfg"
fi

############################################################
# Install systemd service
############################################################

echo "Installing NozzleVision API service..."

sudo cp moonraker/nozzlevision.service \
    /etc/systemd/system/nozzlevision.service

sudo systemctl daemon-reload
sudo systemctl enable nozzlevision
sudo systemctl restart nozzlevision

############################################################
# Finished
############################################################

echo ""
echo "========================================"
echo " NozzleVision installed successfully!"
echo "========================================"
echo ""
echo "✔ Python environment created"
echo "✔ Dependencies installed"
echo "✔ Klipper configuration copied"
echo "✔ printer.cfg updated"
echo "✔ NozzleVision API installed"
echo "✔ API service started"
echo ""
echo "Please run a 'Firmware Restart' in Klipper."
echo ""
echo "Manual start:"
echo "    ~/NozzleVision/run.sh"
echo ""
echo "API:"
echo "Restarting Moonraker..."

sudo systemctl restart moonraker || true
echo "    http://$(hostname -I | awk '{print $1}'):5050/check"