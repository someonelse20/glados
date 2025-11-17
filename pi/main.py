import socket

#from movement import main

#main.record('calm')

SELF_IP = '0.0.0.0'
SERVER_IP = '10.0.0.109'
PI_TO_SERVER_PORT = 5000
SERVER_TO_PI_PORT = 5001
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print ("Socket successfully created")


s.connect((SERVER_IP, PI_TO_SERVER_PORT))

with open('testfile.txt', 'rb') as file:
    while True:
        bytes_read = file.read(BUFFER_SIZE)
        if not bytes_read:
            break

        s.sendall(bytes_read)
    s.close()

