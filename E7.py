# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: XOR the bytes of b'secret' with key 0x10 and print the result

msg = b"secret"  # message to XOR
key = 0x10       # XOR key (integer)
xored = bytes([b ^ key for b in msg])  # XOR each byte
print("XOR result:", xored)
