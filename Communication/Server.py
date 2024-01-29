import socket

s = socket.socket()

print('Socket Created!')

s.bind(('localhost', 9999))
s.listen()

print('Waiting for connection ...')

conn = True

while conn:
    c, addr = s.accept()

    print('\nConnection established from ', addr)

    msg_rcv = c.recv(1024).decode()

    print('Client: ', msg_rcv)

    if msg_rcv == 'exit':
        c.send(bytes('connection disclose', 'UTF-8'))
        conn = False
        break

    msg_send = input('Server: ')

    c.send(bytes(msg_send, 'UTF-8'))

c.close()
s.close()