# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: Convert strings to bytes, hex and back again

# Define a simple string
s = "Cyber"

# Convert string to bytes
b = s.encode()
print("Encoded to bytes:", b)

# Convert bytes to hex
h = b.hex()
print("Bytes to hex:", h)

# Convert hex back to text
restored = bytes.fromhex(h).decode()
print("Hex back to string:", restored)
