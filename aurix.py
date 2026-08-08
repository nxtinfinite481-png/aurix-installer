import os

from assets.banner import banner, clear
from assets.colors import Colors as C

from modules import update
from modules import hostname
from modules import ssh
from modules import tailscale
from modules import docker
from modules import panel
from modules import cloudflare
from modules import wings
from modules import addons


def system_info():

    hostname_name = os.popen("hostname").read().strip()

    os_name = os.popen("grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '\"'").read().strip()

    ram = os.popen("free -h | awk '/Mem:/ {print $3\" / \"$2}'").read().strip()

    disk = os.popen("df -h / | awk 'NR==2 {print $3\" / \"$2}'").read().strip()

    ip = os.popen("tailscale ip -4 2>/dev/null").read().strip()

    if ip == "":
        ip = "Not Connected"

    print(f"{C.BRIGHT_WHITE}═══════════════════════════════════════════════════════")
    print(f"{C.BRIGHT_CYAN}                 AURIX INSTALLER")
    print(f"{C.BRIGHT_WHITE}                   Made by INFINITE")
    print(f"{C.BRIGHT_WHITE}═══════════════════════════════════════════════════════")

    print(f"""
{C.BRIGHT_GREEN}Hostname : {C.WHITE}{hostname_name}

{C.BRIGHT_GREEN}OS       : {C.WHITE}{os_name}

{C.BRIGHT_GREEN}RAM      : {C.WHITE}{ram}

{C.BRIGHT_GREEN}Disk     : {C.WHITE}{disk}

{C.BRIGHT_GREEN}Tail IP  : {C.WHITE}{ip}
""")


def dashboard():

    while True:

        clear()

        banner()

        system_info()

        print(f"""
{C.BRIGHT_MAGENTA}
═══════════════ SYSTEM ═══════════════

{C.BRIGHT_YELLOW}[1]{C.WHITE} Update & Upgrade

{C.BRIGHT_YELLOW}[2]{C.WHITE} Hostname

{C.BRIGHT_YELLOW}[3]{C.WHITE} SSH

{C.BRIGHT_YELLOW}[4]{C.WHITE} Tailscale


{C.BRIGHT_MAGENTA}
════════════ PTERODACTYL ════════════

{C.BRIGHT_YELLOW}[5]{C.WHITE} Docker

{C.BRIGHT_YELLOW}[6]{C.WHITE} Panel

{C.BRIGHT_YELLOW}[7]{C.WHITE} Cloudflare

{C.BRIGHT_YELLOW}[8]{C.WHITE} Wings

{C.BRIGHT_YELLOW}[9]{C.WHITE} Addons


{C.BRIGHT_RED}[0]{C.WHITE} Exit
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":
            update.run()

        elif choice == "2":
            hostname.run()

        elif choice == "3":
            ssh.run()

        elif choice == "4":
            tailscale.run()

        elif choice == "5":
            docker.run()

        elif choice == "6":
            panel.run()

        elif choice == "7":
            cloudflare.run()

        elif choice == "8":
            wings.run()

        elif choice == "9":
            addons.run()

        elif choice == "0":

            clear()

            print(f"""{C.BRIGHT_CYAN}

Thanks for using AURIX.

Made with ❤️ by INFINITE.

{C.RESET}
""")

            break

        else:
            input("\nInvalid Option...")


if __name__ == "__main__":
    dashboard()