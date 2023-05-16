import socket

host='localhost'
port = 9000

s = socket.socket()
s.bind((host,port))

s.listen(1)

c, addr = s.accept()

print('connection accepted from',addr)

while True:

    data = c.recv(1024)
    if not data:
        break
    print("From client:", data.decode())
    
    data1 = input("Enter response:")
    
    c.send(data1.encode())

c.close()
