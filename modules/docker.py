import shutil
import subprocess


def run():
    print("\n================================")
    print("          DOCKER SETUP")
    print("================================\n")

    try:
        docker = shutil.which("docker")

        if docker:
            result = subprocess.run(
                ["docker", "--version"],
                capture_output=True,
                text=True
            )

            print(f"[✓] Docker already installed.")
            print(result.stdout.strip())

        else:
            print("[+] Docker not found.")
            print("[+] Installing Docker...\n")

            subprocess.run(
                ["bash", "-c", "curl -fsSL https://get.docker.com | sh"],
                check=True
            )

        subprocess.run(
            ["systemctl", "enable", "--now", "docker"],
            check=True
        )

        result = subprocess.run(
            ["docker", "--version"],
            capture_output=True,
            text=True,
            check=True
        )

        print("\n[✓] Docker is ready.")
        print(result.stdout.strip())

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
