import socket

host='localhost'
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1) #max connections=1
c,addr=s.accept()
print(type(addr))
print('connection from',str(addr))

c.send(b"Hello client!")
msg="Bye!"
c.send(msg.encode())

c.close()