# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: Complete mini challenge tasks using short Python scripts

import hashlib
import secrets
import string
import datetime
import socket

# Convert hex string to ASCII (from lab sheet)
hex_str = "666c616766616c676e616d6573697365617379"
print("Hex -> ASCII:", bytes.fromhex(hex_str).decode())

# SHA1 of 'CTF2025'
print("SHA1('CTF2025') =", hashlib.sha1(b"CTF2025").hexdigest())

# Random 12 character password (must include one symbol)
chars = string.ascii_letters + string.digits + "!@#$%^&*"
pwd = ''.join(secrets.choice(chars) for _ in range(12))
print("12-character password:", pwd)

# Current date and time in ISO format
print("Current time (ISO):", datetime.datetime.now().isoformat(timespec="seconds"))

# IP of picoctf.com
print("picoctf.com ->", socket.gethostbyname("picoctf.com"))
