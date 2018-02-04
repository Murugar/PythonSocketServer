'''TCP IPv4 client'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 20000))

print(s.recv(1024).decode('utf-8'))
for data in (b'Test1', b'Test2', b'Test3'):
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
