# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: Generate 5 random 16 character passwords using the secrets module

import secrets
import string

# Create a pool of letters and digits
alphabet = string.ascii_letters + string.digits

# Generate and print 5 random passwords
for i in range(5):
    password = ''.join(secrets.choice(alphabet) for _ in range(16))
    print(f"Password {i+1}:", password)
