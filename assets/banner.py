import os
from assets.colors import Colors as C


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():

    print(f"""{C.BRIGHT_CYAN}

 █████╗ ██╗   ██╗██████╗ ██╗██╗  ██╗
██╔══██╗██║   ██║██╔══██╗██║╚██╗██╔╝
███████║██║   ██║██████╔╝██║ ╚███╔╝
██╔══██║██║   ██║██╔══██╗██║ ██╔██╗
██║  ██║╚██████╔╝██║  ██║██║██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝

{C.BRIGHT_WHITE}═══════════════════════════════════════════════════════
{C.BRIGHT_GREEN}               AURIX INSTALLER v1.0
{C.BRIGHT_WHITE}═══════════════════════════════════════════════════════

{C.BRIGHT_CYAN}Made with ❤️ by INFINITE

{C.RESET}""")