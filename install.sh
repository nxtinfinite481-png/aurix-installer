#!/bin/bash

set -e

REPO="https://github.com/nxtinfinite481-png/aurix-installer.git"
INSTALL_DIR="/opt/aurix-installer"

clear

echo "=============================================="
echo "              AURIX INSTALLER"
echo "                 Made by INFINITE"
echo "=============================================="
echo

if [ "$EUID" -ne 0 ]; then
    echo "[ERROR] Please run this installer as root."
    exit 1
fi

echo "[1/5] Updating system..."
apt update -y
apt upgrade -y

echo "[2/5] Installing required packages..."
apt install -y git python3 python3-pip python3-venv curl wget

echo "[3/5] Downloading AURIX..."

if [ -d "$INSTALL_DIR" ]; then
    rm -rf "$INSTALL_DIR"
fi

git clone "$REPO" "$INSTALL_DIR"

cd "$INSTALL_DIR"

echo "[4/5] Installing Python dependencies..."

python3 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "[5/5] Starting AURIX..."

sleep 2

python3 aurix.py
