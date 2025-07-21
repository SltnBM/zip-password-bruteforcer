import zipfile
import argparse

def brute_force_zip(zip_path, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist_path}")
        return

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            try:
                zip_file.extractall()
                print("[*] ZIP is not password protected.")
                return
            except RuntimeError:
                pass
    except FileNotFoundError:
        print(f"[!] ZIP file not found: {zip_path}")
        return
    except zipfile.BadZipFile:
        print(f"[!] Invalid or corrupted ZIP file: {zip_path}")
        return

    for password in passwords:
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_file:
                zip_file.extractall(pwd=password.encode())
                print(f"[+] Password found: {password}")
                return password
        except RuntimeError:
            print(f"[-] Incorrect password: {password}")
        except zipfile.BadZipFile:
            print("[!] ZIP file became unreadable during extraction.")
            return
    print("[-] Password not found in the wordlist.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZIP brute force script")
    parser.add_argument('zip_path', nargs='?', help='Path to the ZIP file')
    parser.add_argument('wordlist_path', nargs='?', help='Path to the password wordlist')

    args = parser.parse_args()

    if args.zip_path and args.wordlist_path:
        brute_force_zip(args.zip_path, args.wordlist_path)
    else:
        zip_path = input("Enter ZIP file path: ")
        wordlist_path = input("Enter wordlist file path: ")
        brute_force_zip(zip_path, wordlist_path)
