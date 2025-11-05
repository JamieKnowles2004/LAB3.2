# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: Convert birthday to Unix timestamp and convert a timestamp to a readable date

import datetime

# Convert my birthday (27 November 2004) to Unix timestamp
bday = datetime.datetime(2004, 11, 27)
print("Birthday:", bday)
print("Birthday -> Unix timestamp:", int(bday.timestamp()))

# Convert 1700000000 back to a readable date
timestamp = 1700000000
print("1700000000 ->", datetime.datetime.fromtimestamp(timestamp))
