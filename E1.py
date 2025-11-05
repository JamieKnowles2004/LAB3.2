# Name: Jamie Knowles
# Student Number: C00307559 
# Date: 05/11/25
# Purpose: printing your username using an environment variable

import os

# getenv('USER') reads the system's username environment variable
username = os.getenv('USER')
print("Your username is:", username)