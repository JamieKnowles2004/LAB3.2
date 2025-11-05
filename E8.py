# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: Perform hostname lookup, IP math and system info display

import socket
import ipaddress
import platform

# Resolve hostnames
print("example.com ->", socket.gethostbyname("example.com"))
print("picoctf.com ->", socket.gethostbyname("picoctf.com"))

# Display first 3 IPs in a /24 subnet
net = ipaddress.ip_network("192.168.1.0/24")
print("First three hosts:", list(net.hosts())[:3])

# Show system information
print("Hostname:", socket.gethostname())
print("Kernel version:", platform.release())
