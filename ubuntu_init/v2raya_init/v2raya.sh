#! /usr/bin/bash
wget -qO - https://apt.v2raya.org/key/public-key.asc | sudo tee /etc/apt/keyrings/v2raya.asc
echo "deb [signed-by=/etc/apt/keyrings/v2raya.asc] https://apt.v2raya.org/ v2raya main" | sudo tee /etc/apt/sources.list.d/v2raya.list
sudo apt update
sudo apt-get install v2raya v2ray
# configure v2raya
sudo cp core-hook-pre.py /etc/v2raya/core-hook-pre.py
sudo cp v2raya_conf /etc/default/v2raya
sudo cp v2ray /etc -r 