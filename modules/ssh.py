import os

from assets.banner import banner, clear
from assets.colors import Colors as C


def cmd(command):
    os.system(command)


def status():
    return os.popen("sshd -T | grep passwordauthentication").read().strip()


def menu():

    while True:

        clear()
        banner()

        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")
        print(f"{C.BRIGHT_CYAN}              SSH MANAGER")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════\n")

        print(f"{C.BRIGHT_GREEN}Current Status:{C.WHITE}")
        print(status())
        print()

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Set Root Password

{C.BRIGHT_YELLOW}[2]{C.WHITE} Enable Password Login

{C.BRIGHT_YELLOW}[3]{C.WHITE} Disable Password Login

{C.BRIGHT_YELLOW}[4]{C.WHITE} Restart SSH

{C.BRIGHT_YELLOW}[5]{C.WHITE} Show SSH Status

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":

            clear()
            banner()

            print(f"{C.GREEN}Setting Root Password...\n{C.RESET}")

            cmd("passwd root")

            input("\nPress Enter...")

        elif choice == "2":

            clear()
            banner()

            print(f"{C.GREEN}Enabling Password Authentication...\n{C.RESET}")

            cmd("sed -i 's/^PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config")

            cmd("sed -i 's/^#PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config")

            cmd("sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config.d/60-cloudimg-settings.conf")

            cmd("sed -i 's/^PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config")

            cmd("sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config")

            cmd("systemctl restart ssh")

            print("\nDone!")

            input("\nPress Enter...")

        elif choice == "3":

            clear()
            banner()

            print(f"{C.YELLOW}Disabling Password Authentication...\n{C.RESET}")

            cmd("sed -i 's/^PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config")

            cmd("systemctl restart ssh")

            print("\nDone!")

            input("\nPress Enter...")

        elif choice == "4":

            clear()
            banner()

            cmd("systemctl restart ssh")

            print(f"{C.GREEN}SSH Restarted Successfully.{C.RESET}")

            input("\nPress Enter...")

        elif choice == "5":

            clear()
            banner()

            print(os.popen("sshd -T | grep -E 'passwordauthentication|permitrootlogin|pubkeyauthentication'").read())

            input("\nPress Enter...")

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()