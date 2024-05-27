#!/usr/bin/bash

mkdir -p /home/wenz/.local/share/zufe_ocr/
cp backend.py  backend.sh /home/wenz/.local/share/zufe_ocr/
sudo cp ./ocr_backend.service /etc/systemd/system/
sudo systemctl enable ocr_backend

