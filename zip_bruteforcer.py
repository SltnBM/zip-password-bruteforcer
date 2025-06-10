import zipfile

def brute_force_zip(zip_file_path, wordlist_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            with open(wordlist_path, 'r') as wordlist:
                for line in wordlist:
                    password = line.strip()
                    try:
                        zip_ref.extractall(pwd=password.encode())
                        print(f"[+] Password found: {password}")
                        return password
                    except:
                        print(f"[-] Incorrect: {password}")
        print("[-] Password not found in the wordlist.")
        return None
    except FileNotFoundError:
        print("ZIP file or wordlist not found.")
        return None

if __name__ == "__main__":
    zip_path = input("Enter the path to the ZIP file: ")
    wordlist_path = input("Enter the path to the wordlist: ")
    brute_force_zip(zip_path, wordlist_path)
