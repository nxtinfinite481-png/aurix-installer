#!/bin/bash

clear

echo "========================================="
echo "           AURIX INSTALLER"
echo "             Made by INFINITE"
echo "========================================="
echo

apt update
apt upgrade -y

apt install -y python3 python3-pip curl wget git

echo
echo "[+] Installing Python requirements..."

pip3 install -r requirements.txt

echo
echo "[+] Starting AURIX..."

python3 aurix.py