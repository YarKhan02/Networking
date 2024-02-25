import socket

conn = True

while conn:
    c = socket.socket()

    c.connect(('localhost', 9999))

    to_publish = input('\nProducer: ')

    c.send(bytes(to_publish, 'UTF-8'))

    msg_rcv = c.recv(1024).decode()

    print('Server: ', msg_rcv)

    conn = False
    c.close()