import subprocess


def run():
    print("\n================================")
    print("        HOSTNAME SETUP")
    print("================================\n")

    current = subprocess.getoutput("hostname")
    print(f"Current hostname: {current}\n")

    hostname = input("Enter new hostname: ").strip()

    if not hostname:
        print("\n[ERROR] Hostname cannot be empty.")
        input("Press Enter to continue...")
        return

    try:
        subprocess.run(
            ["hostnamectl", "set-hostname", hostname],
            check=True
        )

        with open("/etc/hosts", "r") as file:
            hosts = file.read()

        lines = hosts.splitlines()
        updated = []

        for line in lines:
            if line.strip().startswith("127.0.1.1"):
                updated.append(f"127.0.1.1\t{hostname}")
            else:
                updated.append(line)

        with open("/etc/hosts", "w") as file:
            file.write("\n".join(updated) + "\n")

        print(f"\n[✓] Hostname changed to: {hostname}")

    except Exception as e:
        print(f"\n[ERROR] {e}")

    input("\nPress Enter to continue...")
