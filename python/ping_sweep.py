import platform
import subprocess
import ipaddress


def ping_host(ip):
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        command = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


def main():
    network = input("Enter network (example: 192.168.1.0/24): ")

    try:
        subnet = ipaddress.ip_network(network, strict=False)
    except ValueError:
        print("Invalid network format.")
        return

    print(f"\nScanning {subnet}...\n")

    online = 0

    for ip in subnet.hosts():
        if ping_host(ip):
            print(f"[+] {ip} is UP")
            online += 1
        else:
            print(f"[-] {ip} is DOWN")

    print(f"\nScan completed.")
    print(f"Online hosts: {online}")


if __name__ == "__main__":
    main()
