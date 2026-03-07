\# Personal Vault

A secure personal vault for passwords, health information, and sensitive data. Built with Python and Tkinter.



\## Features



\*\*Security\*\*

\- Master password authentication on launch with Argon2 hashing

\- AES-128 Fernet encrypted local storage

\- Session timeout after 10 minutes of inactivity

\- HaveIBeenPwned breach checking via k-anonymity — your password never leaves your device

\- Auto clear clipboard 30 seconds after copying a password

\- Password strength indicator



\*\*Vault Entry Types\*\*

\- Passwords

\- Emergency info (blood type, allergies, medications, emergency contacts)

\- Insurance policies

\- Medications and prescriptions

\- Secure notes

\- Credit cards

\- Identity info (passport, drivers license, SSN)

\- WiFi passwords



\*\*Usability\*\*

\- Search, edit, and delete saved entries

\- Category system — Personal, Health, Finance, Family, Work

\- Browse all entries in a searchable, filterable vault view

\- Password generator with letters, symbols, and numbers

\- Copy password to clipboard from search results

\- Show/hide password toggle

\- Clean dark mode UI



\## Requirements

\- Python 3.x

\- cryptography

\- pyperclip

\- argon2-cffi



\## Installation

1\. Clone the repository

2\. Install dependencies: `pip install -r requirements.txt`

3\. Run: `python main.py`



\## Standalone Executable

A prebuilt Windows executable is available in the Releases section.

No Python installation required — just download and run `main.exe`.



Note: `data.bin` and `master.json` will be created in the same folder as the exe.

Keep these files alongside the exe to retain your saved passwords.



\## Security Notes

\- `data.bin` stores your encrypted vault — never share this file

\- `master.json` stores an Argon2 hash of your master password — not the password itself

\- Neither file is included in this repository

\- Breach checking uses k-anonymity — only the first 5 characters of a SHA1 hash are sent to the API, never your actual password



\## Roadmap

This project is under active development. Planned features include cloud sync, native mobile apps (Android and iOS), additional entry types, and AES-256 encryption upgrade. See ROADMAP.md for full details.

