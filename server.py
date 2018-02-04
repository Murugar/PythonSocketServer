import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 20000))
s.listen(5)
print('Waiting for socket connection...')


def tcplink(sock, addr):
    print('Accept new socket connection from  %s:%s...' % addr)
    sock.send(b'Welcome From Socket Server!')
    while True:
        time.sleep(1)
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello from Socket Server, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Socket Connection from %s:%s closed.' % addr)


while True:
    sock, addr = s.accept()
    # print('sock = %s, addr = %s' % (sock, addr))
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
