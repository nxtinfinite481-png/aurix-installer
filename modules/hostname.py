import os

from assets.banner import banner, clear
from assets.colors import Colors as C


def run(command):
    os.system(command)


def current_hostname():
    return os.popen("hostname").read().strip()


def menu():

    while True:

        clear()
        banner()

        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")
        print(f"{C.BRIGHT_CYAN}           CHANGE HOSTNAME")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════\n")

        print(f"{C.BRIGHT_GREEN}Current Hostname : {C.WHITE}{current_hostname()}\n")

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Change Hostname

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":

            new = input("\nEnter New Hostname: ").strip()

            if new == "":
                input("\nHostname cannot be empty...")
                continue

            print("\nChanging Hostname...\n")

            run(f"hostnamectl set-hostname {new}")

            run(f'echo "{new}" > /etc/hostname')

            run(
                f"sed -i 's/127.0.1.1.*/127.0.1.1 {new}/' /etc/hosts"
            )

            print(f"{C.BRIGHT_GREEN}")

            print("✓ Hostname Updated Successfully.")

            print(f"""
Current Hostname : {current_hostname()}

It is recommended to reboot the VPS.

{C.RESET}
""")

            input("Press Enter...")

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()