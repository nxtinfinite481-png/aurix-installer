import os

from assets.banner import banner, clear
from assets.colors import Colors as C


def cmd(command):
    os.system(command)


def output(command):
    return os.popen(command).read().strip()


def menu():

    while True:

        clear()
        banner()

        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")
        print(f"{C.BRIGHT_CYAN}          PTERODACTYL PANEL")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Install Panel

{C.BRIGHT_YELLOW}[2]{C.WHITE} Configure Environment

{C.BRIGHT_YELLOW}[3]{C.WHITE} Change Panel Domain (APP_URL)

{C.BRIGHT_YELLOW}[4]{C.WHITE} Configure Mail

{C.BRIGHT_YELLOW}[5]{C.WHITE} Clear Cache

{C.BRIGHT_YELLOW}[6]{C.WHITE} Restart Queue

{C.BRIGHT_YELLOW}[7]{C.WHITE} Panel Status

{C.BRIGHT_YELLOW}[8]{C.WHITE} Panel Information

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        # ----------------------------------

        if choice == "1":

            clear()
            banner()

            print(f"{C.GREEN}Starting Panel Installer...\n{C.RESET}")

            cmd("bash <(curl -s https://pterodactyl-installer.se)")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "2":

            clear()
            banner()

            print(f"{C.GREEN}Opening Environment Setup...\n{C.RESET}")

            cmd("cd /var/www/pterodactyl && php artisan p:environment:setup")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "3":

            clear()
            banner()

            print()

            current = output("grep APP_URL /var/www/pterodactyl/.env")

            print(f"Current : {current}\n")

            new = input("New Domain : ").strip()

            if new != "":

                cmd(f'''sed -i 's|APP_URL=.*|APP_URL="{new}"|' /var/www/pterodactyl/.env''')

                cmd("cd /var/www/pterodactyl && php artisan config:clear")
                cmd("cd /var/www/pterodactyl && php artisan cache:clear")

                print("\nDone!")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "4":

            clear()
            banner()

            cmd("cd /var/www/pterodactyl && php artisan p:environment:mail")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "5":

            clear()
            banner()

            cmd("cd /var/www/pterodactyl && php artisan optimize:clear")

            print("\nCache Cleared.")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "6":

            clear()
            banner()

            cmd("systemctl restart pteroq")

            print("\nQueue Restarted.")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "7":

            clear()
            banner()

            cmd("systemctl status nginx --no-pager")
            print()
            cmd("systemctl status php8.4-fpm --no-pager")
            print()
            cmd("systemctl status redis-server --no-pager")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "8":

            clear()
            banner()

            cmd("cd /var/www/pterodactyl && php artisan p:info")

            input("\nPress Enter...")

        # ----------------------------------

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()