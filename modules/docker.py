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
        print(f"{C.BRIGHT_CYAN}              DOCKER MANAGER")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════\n")

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Install Docker

{C.BRIGHT_YELLOW}[2]{C.WHITE} Install Docker Compose

{C.BRIGHT_YELLOW}[3]{C.WHITE} Start Docker

{C.BRIGHT_YELLOW}[4]{C.WHITE} Enable Docker

{C.BRIGHT_YELLOW}[5]{C.WHITE} Docker Version

{C.BRIGHT_YELLOW}[6]{C.WHITE} Docker Status

{C.BRIGHT_YELLOW}[7]{C.WHITE} Remove Docker

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":

            clear()
            banner()

            print(f"{C.GREEN}Installing Docker...\n{C.RESET}")

            cmd("curl -fsSL https://get.docker.com | sh")

            input("\nDocker Installed. Press Enter...")

        elif choice == "2":

            clear()
            banner()

            print(f"{C.GREEN}Installing Docker Compose...\n{C.RESET}")

            cmd("apt install docker-compose-plugin -y")

            input("\nDone. Press Enter...")

        elif choice == "3":

            clear()
            banner()

            cmd("systemctl start docker")

            print(f"{C.GREEN}Docker Started.{C.RESET}")

            input("\nPress Enter...")

        elif choice == "4":

            clear()
            banner()

            cmd("systemctl enable docker")

            print(f"{C.GREEN}Docker Enabled at Boot.{C.RESET}")

            input("\nPress Enter...")

        elif choice == "5":

            clear()
            banner()

            print(output("docker --version"))
            print(output("docker compose version"))

            input("\nPress Enter...")

        elif choice == "6":

            clear()
            banner()

            print(output("systemctl status docker --no-pager"))

            input("\nPress Enter...")

        elif choice == "7":

            clear()
            banner()

            confirm = input("Remove Docker? (y/n): ")

            if confirm.lower() == "y":

                cmd("apt purge docker-ce docker-ce-cli docker-compose-plugin containerd.io -y")
                cmd("apt autoremove -y")
                cmd("rm -rf /var/lib/docker")
                cmd("rm -rf /etc/docker")

                print(f"{C.RED}Docker Removed Successfully.{C.RESET}")

            input("\nPress Enter...")

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()