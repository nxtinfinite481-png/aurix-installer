import os
import sys

from assets.banner import banner


def clear():
    os.system("clear")


def pause():
    input("\nPress Enter to continue...")


def main():
    while True:
        clear()
        banner()

        print("┌──────────────────────────────────────────────┐")
        print("│                 SYSTEM                       │")
        print("├──────────────────────────────────────────────┤")
        print("│ [1] Update & Upgrade                         │")
        print("│ [2] Hostname                                 │")
        print("│ [3] SSH                                      │")
        print("│ [4] Tailscale                                │")
        print("│                                              │")
        print("│               PTERODACTYL                   │")
        print("├──────────────────────────────────────────────┤")
        print("│ [5] Docker                                   │")
        print("│ [6] Panel                                    │")
        print("│ [7] Cloudflare                               │")
        print("│ [8] Wings                                    │")
        print("│ [9] Addons                                   │")
        print("│                                              │")
        print("│ [0] Exit                                     │")
        print("└──────────────────────────────────────────────┘")

        choice = input("\nSelect Option ➜ ").strip()

        try:
            if choice == "1":
                from modules import update
                update.run()

            elif choice == "2":
                from modules import hostname
                hostname.run()

            elif choice == "3":
                from modules import ssh
                ssh.run()

            elif choice == "4":
                from modules import tailscale
                tailscale.run()

            elif choice == "5":
                from modules import docker
                docker.run()

            elif choice == "6":
                from modules import panel
                panel.run()

            elif choice == "7":
                from modules import cloudflare
                cloudflare.run()

            elif choice == "8":
                from modules import wings
                wings.run()

            elif choice == "9":
                from modules import addons
                addons.run()

            elif choice == "0":
                clear()
                print("\nAURIX Installer")
                print("Made by INFINITE\n")
                sys.exit(0)

            else:
                print("\n[!] Invalid option.")
                pause()

        except KeyboardInterrupt:
            print("\n\n[!] Operation cancelled.")
            pause()

        except Exception as error:
            print(f"\n[ERROR] {error}")
            pause()


if __name__ == "__main__":
    main()
