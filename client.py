import socket

TEXT_FORMAT = 'utf-8'
BUFFER_SIZE = 1024

HOST = ''
PORT = 8080

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

while True:
    socket.send(input().encode(TEXT_FORMAT))

    message = ''

    while message == '':
        message = socket.recv(BUFFER_SIZE).decode(TEXT_FORMAT)
        if message:
            print(message)
