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
        print(f"{C.BRIGHT_CYAN}            TAILSCALE MANAGER")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════\n")

        print(f"{C.BRIGHT_GREEN}Status:{C.WHITE}")
        print(output("tailscale status 2>/dev/null || echo 'Not Installed'"))

        print()

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Install Tailscale

{C.BRIGHT_YELLOW}[2]{C.WHITE} Login

{C.BRIGHT_YELLOW}[3]{C.WHITE} Show Tailscale IP

{C.BRIGHT_YELLOW}[4]{C.WHITE} Show Status

{C.BRIGHT_YELLOW}[5]{C.WHITE} Enable Auto Start

{C.BRIGHT_YELLOW}[6]{C.WHITE} Logout

{C.BRIGHT_YELLOW}[7]{C.WHITE} Remove Tailscale

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":

            clear()
            banner()

            print(f"{C.GREEN}Installing Tailscale...\n{C.RESET}")

            cmd("curl -fsSL https://tailscale.com/install.sh | sh")

            input("\nInstallation Complete. Press Enter...")

        elif choice == "2":

            clear()
            banner()

            print(f"{C.GREEN}Opening Login...\n{C.RESET}")

            cmd("tailscale up")

            input("\nPress Enter...")

        elif choice == "3":

            clear()
            banner()

            print(f"{C.BRIGHT_CYAN}IPv4:{C.WHITE}")

            print(output("tailscale ip -4"))

            print()

            print(f"{C.BRIGHT_CYAN}IPv6:{C.WHITE}")

            print(output("tailscale ip -6"))

            input("\nPress Enter...")

        elif choice == "4":

            clear()
            banner()

            print(output("tailscale status"))

            input("\nPress Enter...")

        elif choice == "5":

            clear()
            banner()

            cmd("systemctl enable tailscaled")

            cmd("systemctl start tailscaled")

            print(f"{C.GREEN}Auto Start Enabled.{C.RESET}")

            input("\nPress Enter...")

        elif choice == "6":

            clear()
            banner()

            cmd("tailscale logout")

            print(f"{C.YELLOW}Logged Out.{C.RESET}")

            input("\nPress Enter...")

        elif choice == "7":

            clear()
            banner()

            confirm = input("Remove Tailscale? (y/n): ")

            if confirm.lower() == "y":

                cmd("apt remove tailscale -y")

                cmd("rm -rf /var/lib/tailscale")

                print(f"{C.RED}Removed Successfully.{C.RESET}")

            input("\nPress Enter...")

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()