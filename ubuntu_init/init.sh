#!/usr/bin/bash
sudo passwd
sudo apt update
sudo apt upgrade

# fish 
sudo apt-get install fish
sudo usermod $USER --shell $(which fish)
sudo usermod root --shell $(which fish)

sudo apt install gpaste-2
sudo apt-get install ripgrep
sudo apt-get install git
sudo apt-get install vim 
sudo apt-get install htop iotop
sudo apt-get install curl wget axel

# code ms edge
wget -qO - https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/keyrings/microsoft.asc
echo "deb [signed-by=/etc/apt/keyrings/microsoft.asc arch=amd64] https://packages.microsoft.com/repos/edge stable main" | sudo tee /etc/apt/sources.list.d/microsoft-edge.list
echo "deb [signed-by=/etc/apt/keyrings/microsoft.asc arch=amd64] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update
sudo apt-get install microsoft-edge-stable code
# make msegde-q
sudo cp ./microsoft-edge-stable-q /usr/bin
sudo chmod +x /usr/bin/microsoft-edge-stable-q
sed 's|microsoft-edge-stable|microsoft-edge-stable-q|g' /usr/share/applications/microsoft-edge.desktop | sudo tee /usr/share/applications/microsoft-edge-q.desktop

# ibus rime 
sudo apt-get install ibus-rime 

# linuxqq
axel https://dldir1.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.5_240305_amd64_01.deb
sudo apt-get install ./QQ_3.2.5_240305_amd64_01.deb

#jetbrains
sudo apt-get install openjdk-20-jdk
sudo apt-get install fuse
axel https://download-cdn.jetbrains.com.cn/toolbox/jetbrains-toolbox-2.2.3.20090.tar.gz

# ICS/YSYX runtime
sudo apt-get install build-essential
sudo apt-get install man                # on-line reference manual
sudo apt-get install gcc-doc            # on-line reference manual for gcc
sudo apt-get install gdb                # GNU debugger
sudo apt-get install git                # revision control system
sudo apt-get install libreadline-dev    # a library used later
sudo apt-get install libsdl2-dev        # a library used later
sudo apt-get install llvm llvm-dev      # llvm project, which contains libraries used later

#configure vim
#configure fish


