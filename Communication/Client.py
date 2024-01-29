import socket
import os

path = r'C:\Users\YarKhan\Desktop\Python\Socket\Communication\conversation.txt'

conn = True

while conn:
    c = socket.socket()

    try:
        c.connect(('localhost', 9999))

        msg_send = input('\nClient: ')

        c.send(bytes(msg_send, 'UTF-8'))

        msg_rcv = c.recv(1024).decode()

        s = 'Client: '
        s += msg_send

        r = 'Server: '
        r += msg_rcv

        with open(path, 'a') as file:
            file.write(s)
            file.write('\n')
            file.write(r)
            file.write('\n')

        if msg_rcv == 'exit':
            conn = False
            break

        print('Server: ', msg_rcv)

    except ConnectionRefusedError:
        print("\nConnection refused. Make sure the server is running.")
        conn = False
        break
    
    finally:
        c.close()