import socket

from buffer import memory

s = socket.socket()

print('Server Created!')

s.bind(('localhost', 9999))
s.listen()

print('Waiting for connection ...')

conn = True

while conn:
    c, addr = s.accept()

    print('\nConnection established from ', addr)

    data = c.recv(1024).decode()

    if data == 'exit':
        c.send(bytes('connection disclose', 'UTF-8'))
        conn = False
        break

    if data == 'yes':
        content = memory.read()
        c.send(bytes(content, 'UTF-8'))
    else:
        memory.write(data)
        c.send(bytes('Published!', 'UTF-8'))

c.close()
s.close()