import os
import subprocess

from assets.banner import banner, clear
from assets.colors import Colors as C


def run(command):
    os.system(command)


def menu():

    while True:

        clear()
        banner()

        print(f"{C.BRIGHT_WHITE}════════════════════════════════════════════════════")
        print(f"{C.BRIGHT_CYAN}             UPDATE & UPGRADE")
        print(f"{C.BRIGHT_WHITE}════════════════════════════════════════════════════")

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} apt update

{C.BRIGHT_YELLOW}[2]{C.WHITE} apt upgrade -y

{C.BRIGHT_YELLOW}[3]{C.WHITE} apt update && apt upgrade -y

{C.BRIGHT_YELLOW}[4]{C.WHITE} Install Common Packages

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":

            clear()
            banner()
            print(f"{C.GREEN}Running apt update...\n{C.RESET}")
            run("apt update")
            input("\nPress Enter...")

        elif choice == "2":

            clear()
            banner()
            print(f"{C.GREEN}Running apt upgrade...\n{C.RESET}")
            run("apt upgrade -y")
            input("\nPress Enter...")

        elif choice == "3":

            clear()
            banner()
            print(f"{C.GREEN}Updating System...\n{C.RESET}")
            run("apt update && apt upgrade -y")
            input("\nPress Enter...")

        elif choice == "4":

            clear()
            banner()

            print(f"{C.GREEN}Installing Common Packages...\n{C.RESET}")

            run(
                "apt install -y "
                "curl wget unzip zip nano vim git "
                "software-properties-common "
                "apt-transport-https "
                "ca-certificates "
                "gnupg "
                "lsb-release "
                "htop "
                "net-tools "
                "jq"
            )

            input("\nPress Enter...")

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()