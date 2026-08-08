import subprocess


BLUEPRINT_INSTALLER = (
    "bash <(curl -fsSL "
    "https://raw.githubusercontent.com/hopingboyz/blueprint/main/addon-installer.sh)"
)


def run():
    while True:
        print("\n================================")
        print("           AURIX ADDONS")
        print("================================\n")

        print("[1] Install Blueprint")
        print("[2] Blueprint Information")
        print("[0] Back")

        choice = input("\nSelect Option ➜ ").strip()

        if choice == "1":
            print("\n[+] Starting Blueprint installer...\n")

            try:
                subprocess.run(
                    ["bash", "-c", BLUEPRINT_INSTALLER],
                    check=True
                )
                print("\n[✓] Blueprint installer finished.")
            except subprocess.CalledProcessError:
                print("\n[ERROR] Blueprint installation failed.")

            input("\nPress Enter to continue...")

        elif choice == "2":
            print("\nBlueprint is the addon framework used with")
            print("Pterodactyl for installing compatible addons.")
            print("\nInstaller:")
            print(BLUEPRINT_INSTALLER)

            input("\nPress Enter to continue...")

        elif choice == "0":
            return

        else:
            print("\n[!] Invalid option.")
