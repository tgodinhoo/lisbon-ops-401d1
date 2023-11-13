import subprocess
import time
from datetime import datetime

def ping(host):
    command = ["ping", "-c", "1", host]

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    host_to_ping = "192.168.1.1"  # Replace with the IP address you want to test

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        success = ping(host_to_ping)

        status = "Success" if success else "Failure"
        print(f"[{timestamp}] Status: {status}, Destination IP: {host_to_ping}")

        time.sleep(2)

if __name__ == "__main__":
    main()
