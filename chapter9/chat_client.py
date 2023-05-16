import socket

host = 'localhost'
port = 9000

s = socket.socket()
s.connect((host, port))

data=str(input('Enter client msg: '))

while data !=  'exit':
    s.send(data.encode())

    data1 = s.recv(1024)
    print("From server: ", data1.decode())

    data = str(input('Enter client msg: '))
    
s.close()
    



