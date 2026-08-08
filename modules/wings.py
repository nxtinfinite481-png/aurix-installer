import os

from assets.banner import banner, clear
from assets.colors import Colors as C


CONFIG = "/etc/pterodactyl/config.yml"


def cmd(command):
    os.system(command)


def output(command):
    return os.popen(command).read().strip()


def menu():

    while True:

        clear()
        banner()

        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")
        print(f"{C.BRIGHT_CYAN}            PTERODACTYL WINGS")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Install Wings

{C.BRIGHT_YELLOW}[2]{C.WHITE} Download Node Configuration

{C.BRIGHT_YELLOW}[3]{C.WHITE} Show Current Remote

{C.BRIGHT_YELLOW}[4]{C.WHITE} Change Remote URL

{C.BRIGHT_YELLOW}[5]{C.WHITE} Restart Wings

{C.BRIGHT_YELLOW}[6]{C.WHITE} Wings Status

{C.BRIGHT_YELLOW}[7]{C.WHITE} Wings Logs

{C.BRIGHT_YELLOW}[8]{C.WHITE} Open Config

{C.BRIGHT_YELLOW}[9]{C.WHITE} Check API (401 Test)

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        # -------------------------------------

        if choice == "1":

            clear()
            banner()

            print(f"{C.GREEN}Installing Wings...\n{C.RESET}")

            cmd("bash <(curl -s https://pterodactyl-installer.se)")

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "2":

            clear()
            banner()

            print("""

Go To:

Admin
↓

Nodes

↓

Configuration

↓

Copy

↓

Paste into

/etc/pterodactyl/config.yml

""")

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "3":

            clear()
            banner()

            print(output(f"grep '^remote:' {CONFIG}"))

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "4":

            clear()
            banner()

            remote = input("Panel URL : ").strip()

            cmd(
                f"sed -i 's|^remote:.*|remote: {remote}|' {CONFIG}"
            )

            print("\nUpdated Successfully.")

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "5":

            clear()
            banner()

            cmd("systemctl restart wings")

            print("\nWings Restarted.")

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "6":

            clear()
            banner()

            cmd("systemctl status wings --no-pager")

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "7":

            clear()
            banner()

            cmd("journalctl -u wings -n 100 --no-pager")

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "8":

            clear()
            banner()

            cmd("nano /etc/pterodactyl/config.yml")

        # -------------------------------------

        elif choice == "9":

            clear()
            banner()

            domain = input("Node Domain : ")

            cmd(f"curl -vk https://{domain}/api/system")

            input("\nPress Enter...")

        # -------------------------------------

        elif choice == "0":
            break

        else:

            input("\nInvalid Option...")


def run():
    menu()