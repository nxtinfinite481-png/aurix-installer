import os

from assets.banner import banner, clear
from assets.colors import Colors as C


def cmd(command):
    os.system(command)


def menu():

    while True:

        clear()
        banner()

        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")
        print(f"{C.BRIGHT_CYAN}          ADDONS MANAGER")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Install Blueprint

{C.BRIGHT_YELLOW}[2]{C.WHITE} Install Nebula Theme

{C.BRIGHT_YELLOW}[3]{C.WHITE} Reinstall Blueprint

{C.BRIGHT_YELLOW}[4]{C.WHITE} Remove Blueprint

{C.BRIGHT_YELLOW}[5]{C.WHITE} Blueprint Information

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":

            clear()
            banner()

            print(f"{C.GREEN}Installing Blueprint...\n{C.RESET}")

            cmd("bash <(curl -fsSL https://raw.githubusercontent.com/hopingboyz/blueprint/main/addon-installer.sh)")

            input("\nPress Enter...")

        elif choice == "2":

            clear()
            banner()

            print("""

Nebula Theme

Github:

https://github.com/prplwtf/nebula

Install after Blueprint.

""")

            input("\nPress Enter...")

        elif choice == "3":

            clear()
            banner()

            cmd("bash <(curl -fsSL https://raw.githubusercontent.com/hopingboyz/blueprint/main/addon-installer.sh)")

            input("\nPress Enter...")

        elif choice == "4":

            clear()
            banner()

            print("Remove Blueprint manually if required.")

            input("\nPress Enter...")

        elif choice == "5":

            clear()
            banner()

            print("""

Blueprint Framework

Developer:
HopingBoyz

Installer:

bash <(curl -fsSL https://raw.githubusercontent.com/hopingboyz/blueprint/main/addon-installer.sh)

""")

            input("\nPress Enter...")

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()