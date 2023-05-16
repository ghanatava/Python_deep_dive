import socket 

host='localhost'
port = 6767
s=socket.socket()

s.bind((host,port))

# max connections=1
s.listen(1)
c,addr=s.accept()
print('Connection accepted from ',addr)

fname = c.recv(1024)

fname = str(fname.decode())

print(f'{fname} recieved from {addr}')

try:
    f=open(fname,'rb')
    content=f.read()

    c.send(content)

    print(f'{fname} sent to {addr}')
    f.close()

except FileNotFoundError:
    c.send(b'File not found')
    c.close()

finally:
    c.close()


