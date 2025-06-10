import zipfile
import argparse

def brute_force(zip_file_path, wordlist_path):
    if not zipfile.is_zipfile(zip_file_path):
        print("[-] The provided file is not a valid ZIP archive.")
        return None
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            with open(wordlist_path, 'r') as wordlist:
                for line in wordlist:
                    password = line.strip()
                    try:
                        zip_ref.extractall(pwd=password.encode())
                        print(f"[+] Password found: {password}")
                        return password
                    except RuntimeError:
                        print(f"[-] Incorrect: {password}")
        print("[-] Password not found in the wordlist.")
        return None
    except FileNotFoundError:
        print("ZIP file or wordlist not found.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZIP Password Brute Forcer")
    parser.add_argument("zip_path", nargs='?', help="Path to the ZIP file")
    parser.add_argument("wordlist_path", nargs='?', help="Path to the wordlist file")

    args = parser.parse_args()

    if args.zip_path and args.wordlist_path:
        brute_force(args.zip_path, args.wordlist_path)
    else:
        zip_path = input("Enter the path to the ZIP file: ")
        wordlist_path = input("Enter the path to the wordlist: ")
        brute_force(zip_path, wordlist_path)
