import os
import subprocess


def run():
    print("\n================================")
    print("       PTERODACTYL PANEL")
    print("================================\n")

    if os.path.exists("/var/www/pterodactyl"):
        print("[✓] Pterodactyl Panel directory already exists.")
        print("[!] Panel may already be installed.")
        input("\nPress Enter to continue...")
        return

    print("[!] Pterodactyl Panel installation will begin.")
    print("[!] Follow the installer prompts carefully.\n")

    confirm = input("Continue? [y/N]: ").strip().lower()

    if confirm != "y":
        print("\n[!] Installation cancelled.")
        input("Press Enter to continue...")
        return

    try:
        command = (
            "bash <(curl -s https://pterodactyl-installer.se)"
        )

        subprocess.run(
            ["bash", "-c", command],
            check=True
        )

        print("\n[✓] Panel installer finished.")

    except subprocess.CalledProcessError:
        print("\n[ERROR] Pterodactyl installer failed.")

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
