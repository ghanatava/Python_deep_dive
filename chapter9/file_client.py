import socket

host = 'localhost'
port = 6767

s = socket.socket()
s.connect((host,port))

fname=input("enter file name: ")

s.send(fname.encode())

content = s.recv(1024)

print(content.decode())

s.close()