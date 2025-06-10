# 🔐 ZIP Password Bruteforcer
A simple Python script to brute-force password-protected ZIP files using a wordlist.


## ✨ Features
- Brute-force ZIP passwords using a custom wordlist
- Supports CLI arguments or interactive input
- Simple and lightweight

## 📋 Requirements
1. Python 3.6+
2. No external libraries required

## 🚀 How to Use
1. Make sure you have Python installed (Python 3.6 or higher recommended). Download it from python.org.
2. Clone the repository.
```bash
git clone https://github.com/username/zip-password-bruteforcer.git
```

3. Navigate to the project directory.
```bash
cd zip-password-bruteforcer
```

4. Run the script.
```bash
python zip_bruteforcer.py
```

## 💻 Usage
Option 1: With CLI arguments
```bash
python zip_bruteforcer.py <path_to_zip> <path_to_wordlist>
```
Example:
```bash
python zip_bruteforcer.py protected.zip wordlist.txt
```

Option 2: Interactive mode
If no arguments are provided, the script will ask for input:
```bash
python zip_bruteforcer.py
```
Example:
```bash
Enter the path to the ZIP file: protected.zip
Enter the path to the wordlist: wordlist.txt
[-] Incorrect: 1234
[-] Incorrect: admin
[-] Incorrect: password
[+] Password found: secret
```

## ⚠️ Disclaimer
This tool is for educational and authorized testing purposes only.
Do not use it on files you do not own or have permission to test.

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

## 📜 License
This project is open-source and free to use.