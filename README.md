# AURIX Installer

> 🚀 Simple VPS installer for AURIX infrastructure  
> Made by **INFINITE**

AURIX Installer is a menu-based installer designed to simplify common VPS and Pterodactyl setup tasks.

---

## ✨ Features

- System Update & Upgrade
- Hostname Configuration
- SSH Configuration
- Tailscale Installation
- Docker Installation
- Pterodactyl Panel Setup
- Cloudflare Tunnel Setup
- Pterodactyl Wings Setup
- Pterodactyl Addons / Blueprint
- Simple interactive menu

---

## 📦 One-Line Installation

Run this command on a fresh Ubuntu VPS:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/nxtinfinite481-png/aurix-installer/main/install.sh)

---

## ▶️ Run AURIX Again

After the first installation, you **do not need to run `install.sh` again**.

To open the AURIX Installer menu again:

```bash
cd /opt/aurix-installer && source .venv/bin/activate && python3 aurix.py
