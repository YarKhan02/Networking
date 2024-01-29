import socket

s = socket.socket()

print('Socket Created!')

s.bind(('localhost', 9999))
s.listen()

print('Waiting for connection ...')

conn = True

while conn:
    c, addr = s.accept()

    print('\nConnection established form ', addr)

    msg_rcv = c.recv(1024).decode()

    if msg_rcv == 'exit':
        c.send(bytes('connection disclose', 'UTF-8'))
        conn = False
        break

    msg_rcv = int(msg_rcv)

    if msg_rcv >= 80:
        c.send(bytes('A Grade', 'UTF-8'))
    elif msg_rcv >= 70 and msg_rcv < 80:
        c.send(bytes('B Grade', 'UTF-8'))
    elif msg_rcv >= 60 and msg_rcv < 70:
        c.send(bytes('C Grade', 'UTF-8'))
    elif msg_rcv >= 50 and msg_rcv < 60:
        c.send(bytes('D Grade', 'UTF-8'))
    else:
        c.send(bytes('F Grade', 'UTF-8'))

c.close()
s.close()