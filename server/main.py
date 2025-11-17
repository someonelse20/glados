import socket

SELF_IP = '0.0.0.0'
PI_IP = '10.15.94.33'
PI_TO_SERVER_PORT = 5000
SERVER_TO_PI_PORT = 5001
BUFFER_SIZE = 4096

s = socket.socket()
s.bind((SELF_IP, PI_TO_SERVER_PORT))
s.listen()

client_socket, address = s.accept()

with open('testfile.txt', 'wb') as file:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        file.write(bytes_read)

client_socket.close()
s.close()

with open('testfile.txt', 'r') as file:
    for line in file.read(): 
        print(line)

