
import socket

TEXT_FORMAT = 'utf-8'
BUFFER_SIZE = 1024

HOST = ''
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communicationSocket, address = server.accept()
    print(f"{address} is now connected!")

    while True:
        message = communicationSocket.recv(BUFFER_SIZE).decode(TEXT_FORMAT)
        if message != '':
            print(message)
            communicationSocket.send(input().encode(TEXT_FORMAT))


# not currently being processed
communicationSocket.close()
print("TCP connection was closed")