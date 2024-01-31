from vidstream import AudioSender
from vidstream import AudioReceiver

import threading

import socket

# The script should be run on both machines 

ip = socket.gethostbyname(socket.gethostname())

receiver = AudioReceiver(ip, 9999)
receive_thread = threading.Thread(target = receiver.start_server)

sender = AudioSender('192.168.10.7', 5555) # Another machine local ip
sender_thread = threading.Thread(target = sender.start_stream)

receiver_thread.start()
sender_thread.start()