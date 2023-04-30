#A program to get ip address of a website

import socket

host='www.google.co.in'

try:
    addr=socket.gethostbyname(host)
    print('IP address of host = '+addr)

except socket.gaierror:
    print('Host not found')
