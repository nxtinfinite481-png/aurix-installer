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
        print(f"{C.BRIGHT_CYAN}         CLOUDFLARE TUNNEL")
        print(f"{C.BRIGHT_WHITE}══════════════════════════════════════════════")

        print(f"""
{C.BRIGHT_YELLOW}[1]{C.WHITE} Install Cloudflared

{C.BRIGHT_YELLOW}[2]{C.WHITE} Login

{C.BRIGHT_YELLOW}[3]{C.WHITE} Create Tunnel

{C.BRIGHT_YELLOW}[4]{C.WHITE} List Tunnels

{C.BRIGHT_YELLOW}[5]{C.WHITE} Route DNS

{C.BRIGHT_YELLOW}[6]{C.WHITE} Create Config File

{C.BRIGHT_YELLOW}[7]{C.WHITE} Install Service

{C.BRIGHT_YELLOW}[8]{C.WHITE} Tunnel Status

{C.BRIGHT_YELLOW}[9]{C.WHITE} Restart Tunnel

{C.BRIGHT_RED}[0]{C.WHITE} Back
""")

        choice = input(f"{C.BRIGHT_CYAN}Select Option ➜ {C.RESET}")

        if choice == "1":

            clear()
            banner()

            print(f"{C.GREEN}Installing Cloudflared...\n{C.RESET}")

            cmd("wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb")
            cmd("dpkg -i cloudflared-linux-amd64.deb")

            input("\nPress Enter...")

        elif choice == "2":

            clear()
            banner()

            cmd("cloudflared tunnel login")

            input("\nPress Enter...")

        elif choice == "3":

            clear()
            banner()

            name = input("Tunnel Name : ")

            cmd(f"cloudflared tunnel create {name}")

            input("\nPress Enter...")

        elif choice == "4":

            clear()
            banner()

            print(output("cloudflared tunnel list"))

            input("\nPress Enter...")

        elif choice == "5":

            clear()
            banner()

            tunnel = input("Tunnel Name : ")
            domain = input("Domain : ")

            cmd(f"cloudflared tunnel route dns {tunnel} {domain}")

            input("\nPress Enter...")

        elif choice == "6":

            clear()
            banner()

            print(f"""
Create:

/etc/cloudflared/config.yml

Example:

tunnel: YOUR-ID

credentials-file:
/root/.cloudflared/YOUR-ID.json

protocol: http2

ingress:

- hostname: panel.example.com
  service: http://localhost:80

- hostname: node.example.com
  service: http://localhost:443

- service: http_status:404
""")

            input("\nPress Enter...")

        elif choice == "7":

            clear()
            banner()

            cmd("cloudflared service install")

            input("\nPress Enter...")

        elif choice == "8":

            clear()
            banner()

            print(output("systemctl status cloudflared --no-pager"))

            input("\nPress Enter...")

        elif choice == "9":

            clear()
            banner()

            cmd("systemctl restart cloudflared")

            print("\nTunnel Restarted.")

            input("\nPress Enter...")

        elif choice == "0":
            break

        else:
            input("\nInvalid Option...")


def run():
    menu()