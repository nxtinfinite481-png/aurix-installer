import subprocess


def run():
    print("\n================================")
    print("          DOCKER SETUP")
    print("================================\n")

    try:
        installed = subprocess.run(
            ["docker", "--version"],
            capture_output=True,
            text=True
        )

        if installed.returncode == 0:
            print(f"[✓] Docker already installed:")
            print(installed.stdout.strip())
        else:
            print("[+] Installing Docker...\n")

            subprocess.run(
                ["bash", "-c", "curl -fsSL https://get.docker.com | sh"],
                check=True
            )

        subprocess.run(
            ["systemctl", "enable", "--now", "docker"],
            check=True
        )

        print("\n[✓] Docker service is running.")

        result = subprocess.run(
            ["docker", "--version"],
            capture_output=True,
            text=True
        )

        print(f"[✓] {result.stdout.strip()}")

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
