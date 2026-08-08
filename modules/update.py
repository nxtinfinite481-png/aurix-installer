import subprocess


def run():
    print("\n[+] Updating system...\n")

    commands = [
        ["apt", "update"],
        ["apt", "upgrade", "-y"],
    ]

    for command in commands:
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            print(f"\n[ERROR] Command failed: {' '.join(command)}")
            return

    print("\n[✓] System update completed.\n")
    input("Press Enter to continue...")
