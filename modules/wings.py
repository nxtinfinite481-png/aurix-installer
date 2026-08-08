import os
import subprocess


def run():
    print("\n================================")
    print("        PTERODACTYL WINGS")
    print("================================\n")

    try:
        os.makedirs("/etc/pterodactyl", exist_ok=True)

        installed = subprocess.run(
            ["wings", "--version"],
            capture_output=True,
            text=True
        )

        if installed.returncode == 0:
            print("[✓] Wings is already installed.")
            print(installed.stdout.strip())
        else:
            print("[+] Downloading Wings...\n")

            subprocess.run(
                [
                    "bash",
                    "-c",
                    "curl -L -o /usr/local/bin/wings "
                    "https://github.com/pterodactyl/wings/releases/latest/download/wings_linux_amd64"
                ],
                check=True
            )

            subprocess.run(
                ["chmod", "u+x", "/usr/local/bin/wings"],
                check=True
            )

            print("\n[✓] Wings installed.")

        print("\n--------------------------------")
        print("Wings configuration")
        print("--------------------------------")

        config = "/etc/pterodactyl/config.yml"

        if os.path.exists(config):
            print("[✓] Wings config.yml found.")
        else:
            print("[!] Wings config.yml not found.")
            print("\nCreate the node in your Pterodactyl Panel first.")
            print("Then download/copy the generated Wings configuration")
            print(f"to:\n{config}")

        service = "/etc/systemd/system/wings.service"

        if not os.path.exists(service):
            with open(service, "w") as file:
                file.write("""[Unit]
Description=Pterodactyl Wings Daemon
After=docker.service
Requires=docker.service

[Service]
User=root
WorkingDirectory=/etc/pterodactyl
LimitNOFILE=4096
PIDFile=/var/run/wings/daemon.pid
ExecStart=/usr/local/bin/wings
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
""")

            subprocess.run(
                ["systemctl", "daemon-reload"],
                check=True
            )

        if os.path.exists(config):
            subprocess.run(
                ["systemctl", "enable", "--now", "wings"],
                check=False
            )

            print("\n[✓] Wings service started.")

            subprocess.run(
                ["systemctl", "--no-pager", "status", "wings"],
                check=False
            )

        else:
            print("\n[!] Wings service was not started because config.yml is missing.")

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
