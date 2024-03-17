#!/usr/bin/bash
# Prerequisites:
sudo apt-get install git help2man perl python3 make autoconf g++ flex bison ccache
sudo apt-get install libgoogle-perftools-dev numactl perl-doc
sudo apt-get install libfl2  # Ubuntu only (ignore if gives error)
sudo apt-get install libfl-dev  # Ubuntu only (ignore if gives error)
sudo apt-get install zlib1g zlib1g-dev  # Ubuntu only (ignore if gives error)

cd ~
git clone https://github.com/verilator/verilator   # Only first time
cd -

# Every time you need to build:
cd ~/verilator
git pull         # Make sure git repository is up-to-date
git checkout v5.008  # Switch to specified release version

autoconf         # Create ./configure script
./configure      # Configure and create Makefile
make -j 10  # Build Verilator itself (if error, try just 'make')
make test -j
sudo make install
cd -