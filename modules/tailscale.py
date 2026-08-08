import shutil
import subprocess


def run():
    print("\n================================")
    print("        TAILSCALE SETUP")
    print("================================\n")

    try:
        if not shutil.which("tailscale"):
            print("[+] Tailscale not found.")
            print("[+] Installing Tailscale...\n")

            subprocess.run(
                [
                    "bash",
                    "-c",
                    "curl -fsSL https://tailscale.com/install.sh | sh"
                ],
                check=True
            )

        print("[✓] Tailscale is installed.\n")

        subprocess.run(
            ["systemctl", "enable", "--now", "tailscaled"],
            check=False
        )

        status = subprocess.run(
            ["tailscale", "status"],
            capture_output=True,
            text=True
        )

        if status.returncode != 0:
            print("[+] Tailscale is not connected.")
            print("[+] Opening Tailscale authentication...\n")

            subprocess.run(
                ["tailscale", "up"],
                check=False
            )
        else:
            print("[✓] Tailscale is already connected.")

        print("\n--------------------------------")
        print("Tailscale IPv4")
        print("--------------------------------")

        subprocess.run(
            ["tailscale", "ip", "-4"],
            check=False
        )

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
