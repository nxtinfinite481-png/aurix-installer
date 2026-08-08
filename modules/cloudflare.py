import os
import subprocess


def run():
    print("\n================================")
    print("       CLOUDFLARE TUNNEL")
    print("================================\n")

    try:
        installed = subprocess.run(
            ["cloudflared", "--version"],
            capture_output=True,
            text=True
        )

        if installed.returncode != 0:
            print("[+] Installing cloudflared...\n")

            subprocess.run(
                ["bash", "-c",
                 "curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o /usr/local/bin/cloudflared"],
                check=True
            )

            subprocess.run(
                ["chmod", "+x", "/usr/local/bin/cloudflared"],
                check=True
            )

        print("[✓] cloudflared is installed.\n")

        print("Choose an option:\n")
        print("[1] Login to Cloudflare")
        print("[2] Create Tunnel")
        print("[3] Route Domain")
        print("[4] Install Tunnel Service")
        print("[5] Check Tunnel")
        print("[0] Back")

        choice = input("\nSelect Option ➜ ").strip()

        if choice == "1":
            subprocess.run(["cloudflared", "tunnel", "login"])

        elif choice == "2":
            name = input("Enter tunnel name: ").strip()

            if name:
                subprocess.run(
                    ["cloudflared", "tunnel", "create", name],
                    check=True
                )

        elif choice == "3":
            tunnel = input("Enter tunnel name/ID: ").strip()
            domain = input("Enter domain: ").strip()

            if tunnel and domain:
                subprocess.run(
                    ["cloudflared", "tunnel", "route", "dns", tunnel, domain],
                    check=True
                )

        elif choice == "4":
            config = "/etc/cloudflared/config.yml"

            if not os.path.exists(config):
                print("\n[ERROR] /etc/cloudflared/config.yml not found.")
                print("Create/configure the tunnel first.")
            else:
                subprocess.run(
                    ["cloudflared", "service", "install"],
                    check=False
                )

                subprocess.run(
                    ["systemctl", "enable", "--now", "cloudflared"],
                    check=False
                )

                print("\n[✓] Cloudflare Tunnel service configured.")

        elif choice == "5":
            subprocess.run(
                ["cloudflared", "tunnel", "list"]
            )

        elif choice == "0":
            return

        else:
            print("\n[!] Invalid option.")

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
