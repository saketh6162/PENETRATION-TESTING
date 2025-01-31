#!/bin/bash

echo "[+] Setting up GR TOOLKIT environment..."

# Folders
mkdir -p logs modules

# Files
touch requirements.txt config.json README.md logs/scan_results.log

# Default content in README.md
echo "# GR TOOLKIT v3.0" > README.md
echo "## Created By GH0ST R1D3R" >> README.md
echo "## Contact: @GH0ST_R1D3R6666" >> README.md
echo "## Telegram Channel: https://t.me/fsociety_reborn" >> README.md

# Default dependencies
echo "requests" > requirements.txt
echo "colorama" >> requirements.txt
echo "bs4" >> requirements.txt
echo "scapy" >> requirements.txt

# Default config.json
echo '{
    "default_target": "127.0.0.1",
    "scan_timeout": 30,
    "report_format": "txt",
    "use_proxy": false
}' > config.json

echo "[+] Setup Complete! Now run your toolkit using: python3 setup.py"
