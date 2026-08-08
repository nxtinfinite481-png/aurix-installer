import subprocess


def run():
    print("\n================================")
    print("        TAILSCALE SETUP")
    print("================================\n")

    try:
        installed = subprocess.run(
            ["which", "tailscale"],
            capture_output=True
        )

        if installed.returncode != 0:
            print("[+] Installing Tailscale...\n")

            subprocess.run(
                ["bash", "-c", "curl -fsSL https://tailscale.com/install.sh | sh"],
                check=True
            )

        subprocess.run(
            ["systemctl", "enable", "--now", "tailscaled"],
            check=True
        )

        status = subprocess.run(
            ["tailscale", "status"],
            capture_output=True,
            text=True
        )

        if status.returncode == 0:
            print("[✓] Tailscale is already connected.")
        else:
            print("[+] Tailscale is not connected.")
            print("\nRun the following command to authenticate:\n")
            print("    tailscale up\n")

            subprocess.run(["tailscale", "up"])

        print("\n--------------------------------")
        print("Tailscale IPv4:")
        print("--------------------------------")

        subprocess.run(["tailscale", "ip", "-4"])

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
