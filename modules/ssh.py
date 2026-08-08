import subprocess


def run():
    print("\n================================")
    print("          SSH SETUP")
    print("================================\n")

    password = input("Enter new root password: ").strip()

    if not password:
        print("\n[ERROR] Password cannot be empty.")
        input("Press Enter to continue...")
        return

    try:
        subprocess.run(
            ["bash", "-c", f"echo 'root:{password}' | chpasswd"],
            check=True
        )

        config = "/etc/ssh/sshd_config"

        with open(config, "r") as file:
            content = file.read()

        replacements = {
            "#PermitRootLogin prohibit-password": "PermitRootLogin yes",
            "PermitRootLogin prohibit-password": "PermitRootLogin yes",
            "#PasswordAuthentication yes": "PasswordAuthentication yes",
            "PasswordAuthentication no": "PasswordAuthentication yes",
        }

        for old, new in replacements.items():
            content = content.replace(old, new)

        with open(config, "w") as file:
            file.write(content)

        subprocess.run(["systemctl", "restart", "ssh"], check=True)

        result = subprocess.run(
            ["sshd", "-T"],
            capture_output=True,
            text=True,
            check=True
        )

        print("\n[✓] SSH password authentication enabled.")

        for line in result.stdout.splitlines():
            if any(x in line for x in [
                "passwordauthentication",
                "permitrootlogin",
                "pubkeyauthentication"
            ]):
                print(line)

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
