# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: Use hashlib and base64 to hash and encode data

import hashlib
import base64

# Compute SHA-256 hash of your name
name = b"Jamie Knowles"
sha256_hash = hashlib.sha256(name).hexdigest()
print("SHA-256('Jamie Knowles') =", sha256_hash)

# Base64 encode the word "security"
encoded = base64.b64encode(b"security").decode()
print("Base64 encoded 'security' =", encoded)

# Decode the given Base64 string
decoded = base64.b64decode("ZmxhZ19pc19saWZlCg==").decode()
print("Decoded Base64 string =", repr(decoded))  # repr shows newline characters
