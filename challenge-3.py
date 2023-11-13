import subprocess
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def ping(host):
    command = ["ping", "-c", "1", host]

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def send_email(subject, body, to_email, from_email, password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 587) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def main():
    host_to_ping = "192.168.1.1"
    
    admin_email = input("Enter your email address: ")
    admin_password = input("Enter your email password: ")

    previous_status = None

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        success = ping(host_to_ping)

        status = "Up" if success else "Down"

        if previous_status is None:
            previous_status = status
        elif previous_status != status:
            subject = "Host Status Change Notification"
            body = f"Host status changed:\nHost: {host_to_ping}\nPrevious Status: {previous_status}\nCurrent Status: {status}\nTimestamp: {timestamp}"
            send_email(subject, body, admin_email, admin_email, admin_password)
            previous_status = status

        print(f"[{timestamp}] Status: {status}, Destination IP: {host_to_ping}")

        time.sleep(2)

if __name__ == "__main__":
    main()
