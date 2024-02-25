import socket


conn = True

while conn:
    c = socket.socket()

    try:
        c.connect(('localhost', 9999))

        msg_send = input('\nSurf: ')

        c.send(bytes(msg_send, 'UTF-8'))

        msg_rcv = c.recv(1024).decode()

        if msg_rcv == 'exit':
            conn = False
            break

        print('Content:\n', msg_rcv)

    except ConnectionRefusedError:
        print("\nConnection refused. Make sure the server is running.")
        conn = False
        break
    
    finally:
        c.close()