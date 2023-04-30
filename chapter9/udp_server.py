import socket
import time

host='localhost'
port=5001

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

time.sleep(5)

s.sendto(b"Hello client, how are you",(host,port))

msg="BYE!"

s.sendto(msg.encode(),(host,port))

s.close()